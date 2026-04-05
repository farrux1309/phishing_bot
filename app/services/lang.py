LANGUAGES = {
    "uz": {
        "start": (
            "👋 Salom! Men phishing linklarni aniqlayman.\n\n"
            "🔗 Menga istalgan link yuboring — tekshirib beraman!\n\n"
            "🌐 Til tanlash uchun /lang yozing.\n"
            "❓ Yordam uchun /help yozing."
        ),
        "help": (
                    "ℹ️ Foydalanish:\n"
                    "1. Menga link yuboring\n"
                    "2. Menga fayl yuboring\n"
                    "3. Men VirusTotal + AI bilan tekshiraman\n"
                    "4. Natijani ko'rsataman\n\n"
                    "🧠 Risk Score nima?\n"
                    "🟢 0-39 — Xavfsiz\n"
                    "🟡 40-69 — Shubhali\n"
                    "🔴 70-100 — Xavfli"
),
        "choose_lang": "🌐 Tilni tanlang:",
        "lang_set": "✅ Til o'zgartirildi: O'zbek 🇺🇿",
        "analyzing": "🔍 Tekshirilmoqda...",
        "not_url": "⚠️ URL https:// bilan boshlanishi kerak",
        "error": "❌ Xatolik yuz berdi, qayta urining.",
        "safe": "✅ Xavfsiz foydalanishingiz mumkin.",
        "warning": "⚠️ Ehtiyot bo'ling!",
    },
    "ru": {
        "start": (
            "👋 Привет! Я определяю фишинговые ссылки.\n\n"
            "🔗 Отправьте мне любую ссылку — проверю!\n\n"
            "🌐 Для смены языка напишите /lang.\n"
            "❓ Помощь: /help"
        ),
        "help": (
                    "ℹ️ Использование:\n"
                    "1. Отправьте ссылку\n"
                    "2. Отправьте файл\n"
                    "3. Я проверю через VirusTotal + AI\n"
                    "4. Покажу результат\n\n"
                    "🧠 Что такое Risk Score?\n"
                    "🟢 0-39 — Безопасно\n"
                    "🟡 40-69 — Подозрительно\n"
                    "🔴 70-100 — Опасно"
),
        "choose_lang": "🌐 Выберите язык:",
        "lang_set": "✅ Язык изменён: Русский 🇷🇺",
        "analyzing": "🔍 Проверяется...",
        "not_url": "⚠️ URL должен начинаться с https://",
        "error": "❌ Произошла ошибка, попробуйте снова.",
        "safe": "✅ Можно использовать безопасно.",
        "warning": "⚠️ Будьте осторожны!",
    },
    "en": {
        "start": (
            "👋 Hello! I detect phishing links.\n\n"
            "🔗 Send me any link — I'll check it!\n\n"
            "🌐 To change language type /lang.\n"
            "❓ Help: /help"
        ),
        "help": (
                    "ℹ️ How to use:\n"
                    "1. Send me a link\n"
                    "2. Send me a file\n"
                    "3. I'll check it via VirusTotal + AI\n"
                    "4. I'll show the result\n\n"
                    "🧠 What is Risk Score?\n"
                    "🟢 0-39 — Safe\n"
                    "🟡 40-69 — Suspicious\n"
                    "🔴 70-100 — Dangerous"
),
        "choose_lang": "🌐 Choose language:",
        "lang_set": "✅ Language changed: English 🇬🇧",
        "analyzing": "🔍 Analyzing...",
        "not_url": "⚠️ URL must start with https://",
        "error": "❌ An error occurred, please try again.",
        "safe": "✅ Safe to use.",
        "warning": "⚠️ Be careful!",
    }
}

# Foydalanuvchi tili saqlanadi
user_langs = {}

def get_lang(user_id):
    return user_langs.get(user_id, "uz")

def set_lang(user_id, lang):
    user_langs[user_id] = lang

def t(user_id, key):
    lang = get_lang(user_id)
    return LANGUAGES[lang][key]