def map_edu(e):
    levels = {"highschool": 0, "associate": 0.3, "bachelor": 0.6, "master": 0.8, "phd": 1.0}
    return levels.get(e.lower(), 0)

def norm(v, a, b): 
    return max(0, min(1, (v - a) / (b - a))) if b > a else 0

def score_applicant(app):
    w = {"experience": 0.2, "education": 0.15, "skills": 0.3, "certifications": 0.1, "interview": 0.25}
    exp = norm(app.get("experience_years", 0), 0, 20)
    edu = map_edu(app.get("education", ""))
    skl = max(0, min(1, app.get("skills_match", 0)))
    cert = norm(app.get("certifications_count", 0), 0, 10)
    intr = norm(app.get("interview_score", 0), 0, 100)

    total = exp*w["experience"] + edu*w["education"] + skl*w["skills"] + cert*w["certifications"] + intr*w["interview"]
    score = round(total / sum(w.values()) * 100, 2)
    return {"score": score, "passed": score >= 65}

def audit_fairness(app):
    base = score_applicant(app)
    variations = [{"name":"John","gender":"male"}, {"name":"Jane","gender":"female"}, {"name":"Jae","gender":"nonbinary"}]
    diffs = [abs(score_applicant({**app, **v})["score"] - base["score"]) for v in variations]
    print("Bias check → mismatch rate:", round(sum(d>1e-6 for d in diffs)/len(diffs), 2))
    return base

# Example applicants
A = {'experience_years':5,'education':'bachelor','skills_match':0.8,'certifications_count':2,'interview_score':85}
B = {'experience_years':1,'education':'highschool','skills_match':0.4,'certifications_count':0,'interview_score':60}

print("A ->", score_applicant(A))
print("B ->", score_applicant(B))
audit_fairness(A)
