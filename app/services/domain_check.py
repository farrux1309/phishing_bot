import whois
from datetime import datetime, timezone

def domain_age(url, lang="uz"):
    try:
        domain = url.split("//")[-1].split("/")[0]
        info = whois.whois(domain)

        creation_date = info.creation_date

        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        if creation_date.tzinfo is not None:
            now = datetime.now(timezone.utc)
        else:
            now = datetime.now()

        age_days = (now - creation_date).days

        if lang == "ru":
            if age_days < 30:
                return f"⚠️ Новый домен ({age_days} дней)"
            else:
                return f"✅ Старый домен ({age_days} дней)"
        elif lang == "en":
            if age_days < 30:
                return f"⚠️ New domain ({age_days} days)"
            else:
                return f"✅ Old domain ({age_days} days)"
        else:
            if age_days < 30:
                return f"⚠️ Yangi domen ({age_days} kun)"
            else:
                return f"✅ Eski domen ({age_days} kun)"

    except:
        if lang == "ru":
            return "❓ Домен не определён"
        elif lang == "en":
            return "❓ Domain not found"
        else:
            return "❓ Domen aniqlanmadi"