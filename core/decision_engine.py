def make_decision(findings, ai_result):

    ai_threat = ai_result == -1
    findings_count = len(findings)

    # Highest severity
    if ai_threat and findings_count >= 1:
        return "High Risk"

    if ai_threat or findings_count >= 3:
        return "High Risk"

    elif findings_count >= 1:
        return "Medium Risk"

    else:
        return "Low Risk"
