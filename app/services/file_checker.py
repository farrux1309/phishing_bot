import requests
import time
from app.core.config import VIRUSTOTAL_API_KEY

def check_file(file_bytes: bytes, filename: str) -> str:
    headers = {"x-apikey": VIRUSTOTAL_API_KEY}

    # 1. FAYLNI YUBORISH
    files = {"file": (filename, file_bytes)}
    response = requests.post(
        "https://www.virustotal.com/api/v3/files",
        headers=headers,
        files=files
    )

    if response.status_code not in [200, 202]:
        return f"❌ API xatolik: {response.status_code}"

    analysis_id = response.json()["data"]["id"]

    # 2. NATIJANI KUTISH
    for _ in range(20):
        time.sleep(4)

        result = requests.get(
            f"https://www.virustotal.com/api/v3/analyses/{analysis_id}",
            headers=headers
        ).json()

        if result["data"]["attributes"]["status"] == "completed":
            stats = result["data"]["attributes"]["stats"]
            malicious = stats.get("malicious", 0)
            suspicious = stats.get("suspicious", 0)
            harmless = stats.get("harmless", 0)
            undetected = stats.get("undetected", 0)

            total = malicious + suspicious + harmless + undetected

            if malicious > 0:
                label = "❌ XAVFLI"
                tavsiya = "⚠️ Bu faylni ochmang!"
            elif suspicious > 0:
                label = "⚠️ SHUBHALI"
                tavsiya = "⚠️ Ehtiyot bo'ling!"
            else:
                label = "✅ XAVFSIZ"
                tavsiya = "✅ Fayl xavfsiz ko'rinadi."

            return (
                f"📁 Fayl tahlili: {filename}\n\n"
                f"{label}\n"
                f"🛡️ VirusTotal: {malicious}/{total} antivirus xavfli dedi\n"
                f"⚠️ Shubhali: {suspicious}/{total}\n"
                f"✅ Xavfsiz: {harmless + undetected}/{total}\n\n"
                f"{tavsiya}"
            )

    return "⏳ Tahlil tugamadi, qayta urining."