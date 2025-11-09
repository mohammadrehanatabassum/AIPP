from copy import deepcopy

def loan_approval(applicant: dict) -> bool:
    """
    Rule-based loan approval that ignores protected attributes (name, gender).
    Expected numeric keys: income, credit_score, debt_to_income, employment_years, loan_amount.
    Returns True for approve, False for deny.
    """
    try:
        income = float(applicant.get("income", 0))
        credit = int(applicant.get("credit_score", 0))
        dti = float(applicant.get("debt_to_income", 999))  # lower is better
        emp_years = int(applicant.get("employment_years", 0))
        loan_amt = float(applicant.get("loan_amount", 0))
    except (TypeError, ValueError):
        return False

    # Basic objective rules (example thresholds)
    if income <= 0 or loan_amt <= 0:
        return False
    if credit < 600:
        return False
    if dti > 0.45:
        return False
    if emp_years < 1:
        return False
    if loan_amt > income * 5:  # affordability heuristic
        return False
    return True


def audit_counterfactual(applicant: dict) -> dict:
    """
    Flip non-financial attributes that should not affect decision (name/gender)
    and check if decision changes.
    """
    original = loan_approval(applicant)
    altered = deepcopy(applicant)
    if "gender" in altered:
        g = altered["gender"]
        altered["gender"] = "female" if str(g).lower().startswith("m") else "male"
    if "name" in altered:
        altered["name"] = altered["name"].swapcase()
    altered_decision = loan_approval(altered)
    return {"original": original, "altered": altered_decision, "match": original == altered_decision}


if __name__ == "__main__":
    # Prompt-variation style examples to test fairness
    examples = [
        {"name": "John", "gender": "male", "income": 60000, "credit_score": 700, "debt_to_income": 0.2, "employment_years": 3, "loan_amount": 150000},
        {"name": "Jane", "gender": "female", "income": 60000, "credit_score": 700, "debt_to_income": 0.2, "employment_years": 3, "loan_amount": 150000},
        {"name": "Alex", "gender": "nonbinary", "income": 35000, "credit_score": 620, "debt_to_income": 0.40, "employment_years": 2, "loan_amount": 80000},
    ]

    for ex in examples:
        decision = loan_approval(ex)
        audit = audit_counterfactual(ex)
        print(f"{ex.get('name')}/{ex.get('gender')}: decision={decision}, audit_match={audit['match']}")

    raw = input("\nEnter applicant as CSV (income,credit_score,dti,employment_years,loan_amount) or press Enter to skip: ").strip()
    if raw:
        try:
            income, credit, dti, emp, loan = raw.split(",")
            app = {"income": float(income), "credit_score": int(credit), "debt_to_income": float(dti),
                   "employment_years": int(emp), "loan_amount": float(loan)}
            print("Decision:", "Approved" if loan_approval(app) else "Denied")
            print("Counterfactual audit:", audit_counterfactual(app))
        except Exception as e:
            print("Invalid input:", e)
