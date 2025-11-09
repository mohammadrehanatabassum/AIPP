# ...existing code...
def score_applicant(app):
    """Gender-neutral job applicant scoring system (ignores name/gender)."""
    weights = {"experience": 0.25, "education": 0.2, "skills": 0.3, "certifications": 0.1, "interview": 0.15}

    # map education levels to numeric scores (0-1)
    edu_map = {"highschool": 0.2, "associate": 0.4, "bachelor": 0.6, "master": 0.8, "phd": 1.0}
    edu = edu_map.get(str(app.get("education", "")).strip().lower(), 0.0)

    # normalize each field to 0-1 with sensible caps
    try:
        exp = min(float(app.get("experience_years", 0)) / 20.0, 1.0)
    except Exception:
        exp = 0.0
    try:
        skills = max(0.0, min(1.0, float(app.get("skills_match", 0.0))))
    except Exception:
        skills = 0.0
    try:
        certs = min(float(app.get("certifications_count", 0)) / 10.0, 1.0)
    except Exception:
        certs = 0.0
    try:
        interview = max(0.0, min(1.0, float(app.get("interview_score", 0)) / 100.0))
    except Exception:
        interview = 0.0

    # score computation (gender-neutral: ignores name/gender)
    total_weight = sum(weights.values()) or 1.0
    raw = (
        exp * weights["experience"]
        + edu * weights["education"]
        + skills * weights["skills"]
        + certs * weights["certifications"]
        + interview * weights["interview"]
    )
    score = round((raw / total_weight) * 100, 2)
    return {"score": score, "passed": score >= 60}


def audit_gender_bias(app):
    """
    Run a small fairness audit by varying name/gender only (including gender-neutral)
    and reporting if scores/decisions change.
    """
    variants = [
        {"name": "Alex", "gender": "male"},
        {"name": "Taylor", "gender": "female"},
        {"name": "Sam", "gender": "nonbinary"},
        {"name": "Jordan", "gender": "gender-neutral"},
    ]
    base = score_applicant(app)
    results = []
    mismatches = 0
    for v in variants:
        test = {**app, **v}  # only non-financial fields change
        res = score_applicant(test)
        match = abs(res["score"] - base["score"]) < 1e-6 and res["passed"] == base["passed"]
        results.append({"variation": v, "score": res["score"], "passed": res["passed"], "match": match})
        if not match:
            mismatches += 1

    mismatch_rate = mismatches / len(variants) if variants else 0.0
    print("Fairness audit: mismatch_rate =", round(mismatch_rate, 3))
    for r in results:
        v = r["variation"]
        print(f"  {v['name']}/{v['gender']}: score={r['score']} passed={r['passed']} match={r['match']}")
    return {"base": base, "results": results, "mismatch_rate": mismatch_rate}


# Changed / added interactive input section
if __name__ == "__main__":
    print("Interactive applicant scoring (press Enter to use default/0).")

    def ask(prompt, cast, default):
        s = input(prompt).strip()
        if not s:
            return default
        try:
            return cast(s)
        except Exception:
            print("Invalid input — using default:", default)
            return default

    experience_years = ask("Experience years (e.g. 5): ", float, 0.0)
    education = input("Education level (highschool/associate/bachelor/master/phd) [bachelor]: ").strip() or "bachelor"
    skills_match = ask("Skills match (0.0 - 1.0) (e.g. 0.8): ", float, 0.0)
    certifications_count = ask("Certifications count (e.g. 2): ", int, 0)
    interview_score = ask("Interview score (0-100) (e.g. 85): ", float, 0.0)

    applicant = {
        "experience_years": experience_years,
        "education": education,
        "skills_match": skills_match,
        "certifications_count": certifications_count,
        "interview_score": interview_score
    }

    result = score_applicant(applicant)
    print("\nResult:", result)
    print("\nRunning fairness audit (name/gender variations including gender-neutral):")
    audit_gender_bias(applicant)