# import requests
# from app.services.ip_check import check_ip
# import time
# from app.core.config import VIRUSTOTAL_API_KEY
# from app.services.risk_score import calculate_risk, risk_label
# from app.services.cache import get_cache, set_cache
# from app.services.domain_check import domain_age
# from app.services.url_utils import is_short_url
# from app.services.lang import t, get_lang
# from app.services.stats import add_check


# def check_url(url: str, user_id: int = None):

#     # 1. LANG (BIRINCHI!)
#     lang = get_lang(user_id) if user_id else "uz"

#     # 2. CACHE CHECK (lang bilan)
#     cached = get_cache(url, lang)
#     if cached:
#         return cached

#     # 3. BASIC VALIDATION
#     if not url.startswith("http"):
#         return t(user_id, "not_url") if user_id else "⚠️ URL https:// bilan boshlanishi kerak"

#     # 4. RISK SCORE
#     score = calculate_risk(url)
#     label = risk_label(score)

#     # 5. EXTRA ANALYSIS
#     age = domain_age(url, lang)
#     short = "🔗 Qisqa link!" if is_short_url(url) else ""

#     headers = {"x-apikey": VIRUSTOTAL_API_KEY}

#     # 6. SEND TO VIRUSTOTAL
#     response = requests.post(
#         "https://www.virustotal.com/api/v3/urls",
#         headers=headers,
#         data={"url": url}
#     )

#     if response.status_code not in [200, 202]:
#         return t(user_id, "error") if user_id else "❌ API xatolik"

#     analysis_id = response.json()["data"]["id"]

#     # 7. WAIT RESULT
#     for _ in range(10):
#         time.sleep(2)

#         result = requests.get(
#             f"https://www.virustotal.com/api/v3/analyses/{analysis_id}",
#             headers=headers
#         ).json()

#         if result["data"]["attributes"]["status"] == "completed":

#             stats = result["data"]["attributes"]["stats"]
#             malicious = stats.get("malicious", 0)
#             suspicious = stats.get("suspicious", 0)
#             harmless = stats.get("harmless", 0)

#             total = malicious + suspicious + harmless

#             # 8. VIRUSTOTAL STATUS
#             if lang == "ru":
#                 if malicious > 0:
#                     vt_status = f"❌ ОПАСНО ({malicious}/{total})"
#                 elif suspicious > 0:
#                     vt_status = f"⚠️ Подозрительно ({suspicious}/{total})"
#                 else:
#                     vt_status = f"✅ Безопасно ({harmless}/{total})"
#             elif lang == "en":
#                 if malicious > 0:
#                     vt_status = f"❌ DANGEROUS ({malicious}/{total})"
#                 elif suspicious > 0:
#                     vt_status = f"⚠️ Suspicious ({suspicious}/{total})"
#                 else:
#                     vt_status = f"✅ Safe ({harmless}/{total})"
#             else:
#                 if malicious > 0:
#                     vt_status = f"❌ XAVFLI ({malicious}/{total})"
#                 elif suspicious > 0:
#                     vt_status = f"⚠️ Shubhali ({suspicious}/{total})"
#                 else:
#                     vt_status = f"✅ Xavfsiz ({harmless}/{total})"

#             # 9. SMART FINAL LOGIC
#             if lang == "ru":
#                 if malicious > 0:
#                     final_label = "❌ ОПАСНО"
#                 elif suspicious > 0 and score >= 80:
#                     final_label = "❌ ОПАСНО (AI + VT)"
#                 elif suspicious > 0:
#                     final_label = "⚠️ ПОДОЗРИТЕЛЬНО"
#                 elif score >= 90:
#                     final_label = "❌ ОПАСНО (AI)"
#                 else:
#                     final_label = label
#             elif lang == "en":
#                 if malicious > 0:
#                     final_label = "❌ DANGEROUS"
#                 elif suspicious > 0 and score >= 80:
#                     final_label = "❌ DANGEROUS (AI + VT)"
#                 elif suspicious > 0:
#                     final_label = "⚠️ SUSPICIOUS"
#                 elif score >= 90:
#                     final_label = "❌ DANGEROUS (AI)"
#                 else:
#                     final_label = label
#             else:
#                 if malicious > 0:
#                     final_label = "❌ XAVFLI"
#                 elif suspicious > 0 and score >= 80:
#                     final_label = "❌ XAVFLI (AI + VT)"
#                 elif suspicious > 0:
#                     final_label = "⚠️ SHUBHALI"
#                 elif score >= 90:
#                     final_label = "❌ XAVFLI (AI)"
#                 else:
#                     final_label = label

#             # 10. TAVSIYA
#             if malicious > 0 or suspicious > 0 or score >= 60:
#                 tavsiya = t(user_id, "warning") if user_id else "⚠️ Ehtiyot bo'ling!"
#             else:
#                 tavsiya = t(user_id, "safe") if user_id else "✅ Xavfsiz."

#             # 11. STATS
#             if malicious > 0 or suspicious > 0:
#                 add_check("malicious")
#             elif score >= 60:
#                 add_check("suspicious")
#             else:
#                 add_check("safe")

#             # 12. FINAL RESPONSE
#             if lang == "en":
#                 header = "🔍 URL Analysis\n"
#                 risk_line = f"🧠 Risk Score: {score}/100"
#                 vt_line = f"🛡️ VirusTotal: {vt_status}"
#             elif lang == "ru":
#                 header = "🔍 Анализ URL\n"
#                 risk_line = f"🧠 Риск: {score}/100"
#                 vt_line = f"🛡️ VirusTotal: {vt_status}"
#             else:
#                 header = "🔍 URL Tahlili\n"
#                 risk_line = f"🧠 Risk Score: {score}/100"
#                 vt_line = f"🛡️ VirusTotal: {vt_status}"

#             parts = [header, final_label, risk_line, vt_line, age]
#             if short:
#                 parts.append(short)
#             parts.append(f"\n{tavsiya}")

#             final = "\n".join(parts)

#             # 13. CACHE SAVE
#             set_cache(url, final, lang)

#             return final

#     return t(user_id, "error") if user_id else "⏳ Tahlil tugamadi"

import requests
import time
from app.services.ssl_check import check_ssl
from app.core.config import VIRUSTOTAL_API_KEY
from app.services.risk_score import calculate_risk, risk_label
from app.services.cache import get_cache, set_cache
from app.services.domain_check import domain_age
from app.services.url_utils import is_short_url
from app.services.lang import t, get_lang
from app.services.stats import add_check
from app.services.ip_check import check_ip


def check_url(url: str, user_id: int = None):

    # 1. LANG (BIRINCHI!)
    lang = get_lang(user_id) if user_id else "uz"

    # 2. CACHE CHECK (lang bilan)
    cached = get_cache(url, lang)
    if cached:
        return cached

    # 3. BASIC VALIDATION
    if not url.startswith("http"):
        return t(user_id, "not_url") if user_id else "⚠️ URL https:// bilan boshlanishi kerak"

    # 4. RISK SCORE
    score = calculate_risk(url)
    label = risk_label(score)

    # 5. EXTRA ANALYSIS
    age = domain_age(url, lang)
    ip_info = check_ip(url)
    ssl_info = check_ssl(url)
    short = "🔗 Qisqa link!" if is_short_url(url) else ""

    headers = {"x-apikey": VIRUSTOTAL_API_KEY}

    # 6. SEND TO VIRUSTOTAL
    response = requests.post(
        "https://www.virustotal.com/api/v3/urls",
        headers=headers,
        data={"url": url}
    )

    if response.status_code not in [200, 202]:
        return t(user_id, "error") if user_id else "❌ API xatolik"

    analysis_id = response.json()["data"]["id"]

    # 7. WAIT RESULT
    for _ in range(10):
        time.sleep(2)

        result = requests.get(
            f"https://www.virustotal.com/api/v3/analyses/{analysis_id}",
            headers=headers
        ).json()

        if result["data"]["attributes"]["status"] == "completed":

            stats = result["data"]["attributes"]["stats"]
            malicious = stats.get("malicious", 0)
            suspicious = stats.get("suspicious", 0)
            harmless = stats.get("harmless", 0)

            total = malicious + suspicious + harmless

            # 8. VIRUSTOTAL STATUS
            if lang == "ru":
                if malicious > 0:
                    vt_status = f"❌ ОПАСНО ({malicious}/{total})"
                elif suspicious > 0:
                    vt_status = f"⚠️ Подозрительно ({suspicious}/{total})"
                else:
                    vt_status = f"✅ Безопасно ({harmless}/{total})"
            elif lang == "en":
                if malicious > 0:
                    vt_status = f"❌ DANGEROUS ({malicious}/{total})"
                elif suspicious > 0:
                    vt_status = f"⚠️ Suspicious ({suspicious}/{total})"
                else:
                    vt_status = f"✅ Safe ({harmless}/{total})"
            else:
                if malicious > 0:
                    vt_status = f"❌ XAVFLI ({malicious}/{total})"
                elif suspicious > 0:
                    vt_status = f"⚠️ Shubhali ({suspicious}/{total})"
                else:
                    vt_status = f"✅ Xavfsiz ({harmless}/{total})"

            # 9. SMART FINAL LOGIC
            if lang == "ru":
                if malicious > 0:
                    final_label = "❌ ОПАСНО"
                elif suspicious > 0 and score >= 80:
                    final_label = "❌ ОПАСНО (AI + VT)"
                elif suspicious > 0:
                    final_label = "⚠️ ПОДОЗРИТЕЛЬНО"
                elif score >= 90:
                    final_label = "❌ ОПАСНО (AI)"
                else:
                    final_label = label
            elif lang == "en":
                if malicious > 0:
                    final_label = "❌ DANGEROUS"
                elif suspicious > 0 and score >= 80:
                    final_label = "❌ DANGEROUS (AI + VT)"
                elif suspicious > 0:
                    final_label = "⚠️ SUSPICIOUS"
                elif score >= 90:
                    final_label = "❌ DANGEROUS (AI)"
                else:
                    final_label = label
            else:
                if malicious > 0:
                    final_label = "❌ XAVFLI"
                elif suspicious > 0 and score >= 80:
                    final_label = "❌ XAVFLI (AI + VT)"
                elif suspicious > 0:
                    final_label = "⚠️ SHUBHALI"
                elif score >= 90:
                    final_label = "❌ XAVFLI (AI)"
                else:
                    final_label = label

            # 10. TAVSIYA
            if malicious > 0 or suspicious > 0 or score >= 60:
                tavsiya = t(user_id, "warning") if user_id else "⚠️ Ehtiyot bo'ling!"
            else:
                tavsiya = t(user_id, "safe") if user_id else "✅ Xavfsiz."

            # 11. STATS
            if malicious > 0 or suspicious > 0:
                add_check("malicious")
            elif score >= 60:
                add_check("suspicious")
            else:
                add_check("safe")

            # 12. FINAL RESPONSE
            if lang == "en":
                header = "🔍 URL Analysis\n"
                risk_line = f"🧠 Risk Score: {score}/100"
                vt_line = f"🛡️ VirusTotal: {vt_status}"
            elif lang == "ru":
                header = "🔍 Анализ URL\n"
                risk_line = f"🧠 Риск: {score}/100"
                vt_line = f"🛡️ VirusTotal: {vt_status}"
            else:
                header = "🔍 URL Tahlili\n"
                risk_line = f"🧠 Risk Score: {score}/100"
                vt_line = f"🛡️ VirusTotal: {vt_status}"

            parts = [header, final_label, risk_line, vt_line, age, ssl_info, ip_info]
            if short:
                parts.append(short)
            parts.append(f"\n{tavsiya}")

            final = "\n".join(parts)

            # 13. CACHE SAVE
            set_cache(url, final, lang)

            return final

    return t(user_id, "error") if user_id else "⏳ Tahlil tugamadi"