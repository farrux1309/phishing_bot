def calculate_risk(url: str):
    score = 0

    url = url.lower()

    # phishing keywords
    keywords = ["login", "verify", "bank", "free", "bonus", "account"]

    for word in keywords:
        if word in url:
            score += 20

    # suspicious patterns
    if url.startswith("http://"):
        score += 15

    if url.count("-") >= 2:
        score += 10

    if len(url) > 75:
        score += 10

    # final limit
    if score > 100:
        score = 100

    return score


def risk_label(score):
    if score >= 70:
        return "❌ XAVFLI"
    elif score >= 40:
        return "⚠️ SHUBHALI"
    else:
        return "✅ XAVFSIZ"