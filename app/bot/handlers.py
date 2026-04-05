# # # from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# # # from telegram.ext import ContextTypes
# # # from app.services.checker import check_url
# # # from app.services.lang import t, set_lang

# # # async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
# # #     user_id = update.message.from_user.id
# # #     await update.message.reply_text(t(user_id, "start"))

# # # async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
# # #     user_id = update.message.from_user.id
# # #     await update.message.reply_text(t(user_id, "help"))

# # # async def lang_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
# # #     user_id = update.message.from_user.id
# # #     keyboard = [
# # #         [
# # #             InlineKeyboardButton("🇺🇿 O'zbek", callback_data="lang_uz"),
# # #             InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru"),
# # #             InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
# # #         ]
# # #     ]
# # #     reply_markup = InlineKeyboardMarkup(keyboard)
# # #     await update.message.reply_text(t(user_id, "choose_lang"), reply_markup=reply_markup)

# # # async def lang_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
# # #     query = update.callback_query
# # #     await query.answer()
# # #     user_id = query.from_user.id
# # #     lang = query.data.split("_")[1]
# # #     set_lang(user_id, lang)
# # #     await query.edit_message_text(t(user_id, "lang_set"))

# # # async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
# # #     user_id = update.message.from_user.id
# # #     text = update.message.text
# # #     await update.message.reply_text(t(user_id, "analyzing"))
# # #     result = check_url(text, user_id)
# # #     await update.message.reply_text(result)

# # from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# # from telegram.ext import ContextTypes
# # from app.services.checker import check_url
# # from app.services.lang import t, set_lang
# # from app.services.stats import add_user

# # async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
# #     user_id = update.message.from_user.id
# #     name = update.message.from_user.full_name
# #     add_user(user_id, name)
# #     await update.message.reply_text(t(user_id, "start"))

# # async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
# #     user_id = update.message.from_user.id
# #     await update.message.reply_text(t(user_id, "help"))

# # async def lang_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
# #     user_id = update.message.from_user.id
# #     keyboard = [
# #         [
# #             InlineKeyboardButton("🇺🇿 O'zbek", callback_data="lang_uz"),
# #             InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru"),
# #             InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
# #         ]
# #     ]
# #     reply_markup = InlineKeyboardMarkup(keyboard)
# #     await update.message.reply_text(t(user_id, "choose_lang"), reply_markup=reply_markup)

# # async def lang_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
# #     query = update.callback_query
# #     await query.answer()
# #     user_id = query.from_user.id
# #     lang = query.data.split("_")[1]
# #     set_lang(user_id, lang)
# #     await query.edit_message_text(t(user_id, "lang_set"))

# # async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
# #     user_id = update.message.from_user.id
# #     name = update.message.from_user.full_name
# #     add_user(user_id, name)
# #     text = update.message.text
# #     await update.message.reply_text(t(user_id, "analyzing"))
# #     result = check_url(text, user_id)
# #     await update.message.reply_text(result)



# # from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# # from telegram.ext import ContextTypes
# # from app.services.checker import check_url
# # from app.services.lang import t, set_lang
# # from app.services.stats import add_user

# # async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
# #     user_id = update.effective_user.id
# #     name = update.effective_user.full_name
# #     add_user(user_id, name)
# #     await update.effective_message.reply_text(t(user_id, "start"))

# # async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
# #     user_id = update.effective_user.id
# #     await update.effective_message.reply_text(t(user_id, "help"))

# # async def lang_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
# #     user_id = update.effective_user.id
# #     keyboard = [
# #         [
# #             InlineKeyboardButton("🇺🇿 O'zbek", callback_data="lang_uz"),
# #             InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru"),
# #             InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
# #         ]
# #     ]
# #     reply_markup = InlineKeyboardMarkup(keyboard)
# #     await update.effective_message.reply_text(
# #         t(user_id, "choose_lang"), reply_markup=reply_markup
# #     )

# # async def lang_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
# #     query = update.callback_query
# #     await query.answer()
# #     user_id = query.from_user.id
# #     lang = query.data.split("_")[1]
# #     set_lang(user_id, lang)
# #     await query.edit_message_text(t(user_id, "lang_set"))

# # async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
# #     user_id = update.effective_user.id
# #     name = update.effective_user.full_name
# #     add_user(user_id, name)

# #     text = update.effective_message.text

# #     # Guruhda faqat link bo'lsa javob bersin
# #     chat_type = update.effective_chat.type
# #     if chat_type in ["group", "supergroup", "channel"]:
# #         if not text.startswith("http"):
# #             return

# #     await update.effective_message.reply_text(t(user_id, "analyzing"))
# #     result = check_url(text, user_id)
# #     await update.effective_message.reply_text(result)





# # from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# # from telegram.ext import ContextTypes
# # from app.services.checker import check_url
# # from app.services.lang import t, set_lang
# # from app.services.stats import add_user
# # from app.services.screenshot import get_screenshot
# # import asyncio

# # async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
# #     user_id = update.effective_user.id
# #     name = update.effective_user.full_name
# #     add_user(user_id, name)
# #     await update.effective_message.reply_text(t(user_id, "start"))

# # async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
# #     user_id = update.effective_user.id
# #     await update.effective_message.reply_text(t(user_id, "help"))

# # async def lang_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
# #     user_id = update.effective_user.id
# #     keyboard = [
# #         [
# #             InlineKeyboardButton("🇺🇿 O'zbek", callback_data="lang_uz"),
# #             InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru"),
# #             InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
# #         ]
# #     ]
# #     reply_markup = InlineKeyboardMarkup(keyboard)
# #     await update.effective_message.reply_text(
# #         t(user_id, "choose_lang"), reply_markup=reply_markup
# #     )

# # async def lang_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
# #     query = update.callback_query
# #     await query.answer()
# #     user_id = query.from_user.id
# #     lang = query.data.split("_")[1]
# #     set_lang(user_id, lang)
# #     await query.edit_message_text(t(user_id, "lang_set"))

# # async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
# #     user_id = update.effective_user.id
# #     name = update.effective_user.full_name
# #     add_user(user_id, name)

# #     text = update.effective_message.text

# #     # Guruhda faqat link bo'lsa javob bersin
# #     chat_type = update.effective_chat.type
# #     if chat_type in ["group", "supergroup", "channel"]:
# #         if not text.startswith("http"):
# #             return

# #     await update.effective_message.reply_text(t(user_id, "analyzing"))
# #     result = check_url(text, user_id)
# #     await update.effective_message.reply_text(result)

# #     # Screenshot olish
# #     if text.startswith("http"):
# #         try:
# #             screenshot = await asyncio.get_event_loop().run_in_executor(
# #                 None, get_screenshot, text
# #             )
# #             if screenshot:
# #                 await update.effective_message.reply_photo(
# #                     photo=screenshot,
# #                     caption="📸 Sayt ko'rinishi"
# #                 )
# #         except:
# #             pass

# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import ContextTypes
# from app.services.checker import check_url
# from app.services.lang import t, set_lang
# from app.services.stats import add_user
# from app.services.screenshot import get_screenshot
# from app.services.file_checker import check_file
# import asyncio

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.effective_user.id
#     name = update.effective_user.full_name
#     add_user(user_id, name)
    
#     await update.effective_message.reply_text(
#         "👋 Salom! Men xavfsizlik botiman.\n\n"
#         "🔗 Link yuboring — tekshirib beraman!\n"
#         "📁 Fayl yuboring — virus bormi tekshiraman!\n\n"
#         "📋 Komandalar:\n"
#         "/help — qo'llanma\n"
#         "/lang — til tanlash\n\n"
#         "❓ Yordam uchun /help yozing."
#     )

# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.effective_user.id
#     await update.effective_message.reply_text(t(user_id, "help"))

# async def lang_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.effective_user.id
#     keyboard = [
#         [
#             InlineKeyboardButton("🇺🇿 O'zbek", callback_data="lang_uz"),
#             InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru"),
#             InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
#         ]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     await update.effective_message.reply_text(
#         t(user_id, "choose_lang"), reply_markup=reply_markup
#     )

# async def lang_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()
#     user_id = query.from_user.id
#     lang = query.data.split("_")[1]
#     set_lang(user_id, lang)
#     await query.edit_message_text(t(user_id, "lang_set"))

# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.effective_user.id
#     name = update.effective_user.full_name
#     add_user(user_id, name)

#     text = update.effective_message.text

#     # Guruhda faqat link bo'lsa javob bersin
#     chat_type = update.effective_chat.type
#     if chat_type in ["group", "supergroup", "channel"]:
#         if not text.startswith("http"):
#             return

#     await update.effective_message.reply_text(t(user_id, "analyzing"))
#     result = check_url(text, user_id)
#     await update.effective_message.reply_text(result)

#     # Screenshot olish
#     if text.startswith("http"):
#         try:
#             screenshot = await asyncio.get_event_loop().run_in_executor(
#                 None, get_screenshot, text
#             )
#             if screenshot:
#                 await update.effective_message.reply_photo(
#                     photo=screenshot,
#                     caption="📸 Sayt ko'rinishi"
#                 )
#         except:
#             pass

# async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.effective_user.id
#     name = update.effective_user.full_name
#     add_user(user_id, name)

#     # Fayl turini aniqlash
#     message = update.effective_message
#     if message.document:
#         file = message.document
#         filename = file.file_name or "unknown"
#     elif message.photo:
#         file = message.photo[-1]
#         filename = "photo.jpg"
#     elif message.video:
#         file = message.video
#         filename = file.file_name or "video.mp4"
#     elif message.audio:
#         file = message.audio
#         filename = file.file_name or "audio.mp3"
#     else:
#         return

#     await message.reply_text(f"📁 Fayl tekshirilmoqda: {filename}...")

#     # Faylni yuklab olish
#     file_obj = await context.bot.get_file(file.file_id)
#     file_bytes = await file_obj.download_as_bytearray()

#     # Tekshirish
#     result = await asyncio.get_event_loop().run_in_executor(
#         None, check_file, bytes(file_bytes), filename
#     )

#     await message.reply_text(result)




from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from app.services.checker import check_url
from app.services.lang import t, set_lang
from app.services.stats import add_user, add_feedback, get_stats
from app.services.screenshot import get_screenshot
from app.services.file_checker import check_file
import asyncio

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    stats = get_stats()

    keyboard = [
        [InlineKeyboardButton("✅ Qo'shilish", callback_data="join")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.effective_message.reply_text(
        f"👥 Foydalanuvchilar: {stats['users']}\n\n"
        "👋 Salom! Men xavfsizlik botiman.\n\n"
        "🔗 Link va fayllarni tekshiraman!\n\n"
        "Botdan foydalanish uchun qo'shiling 👇",
        reply_markup=reply_markup
    )

async def join_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    name = query.from_user.full_name
    add_user(user_id, name)

    await query.edit_message_text(
        "✅ Muvaffaqiyatli qo'shildingiz!\n\n"
        "👋 Xush kelibsiz!\n\n"
        "🔗 Link yuboring — tekshirib beraman!\n"
        "📁 Fayl yuboring — virus bormi tekshiraman!\n\n"
        "📋 Komandalar:\n"
        "/help — qo'llanma\n"
        "/lang — til tanlash\n\n"
        "❓ Yordam uchun /help yozing."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    await update.effective_message.reply_text(t(user_id, "help"))

async def lang_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    keyboard = [
        [
            InlineKeyboardButton("🇺🇿 O'zbek", callback_data="lang_uz"),
            InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru"),
            InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.effective_message.reply_text(
        t(user_id, "choose_lang"), reply_markup=reply_markup
    )

async def lang_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    lang = query.data.split("_")[1]
    set_lang(user_id, lang)
    await query.edit_message_text(t(user_id, "lang_set"))

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    name = update.effective_user.full_name
    add_user(user_id, name)

    text = update.effective_message.text

    # Guruhda faqat link bo'lsa javob bersin
    chat_type = update.effective_chat.type
    if chat_type in ["group", "supergroup", "channel"]:
        if not text.startswith("http"):
            return

    await update.effective_message.reply_text(t(user_id, "analyzing"))
    result = check_url(text, user_id)

    # Feedback tugmalari
    keyboard = [
        [
            InlineKeyboardButton("👍 To'g'ri", callback_data="feedback_correct"),
            InlineKeyboardButton("👎 Noto'g'ri", callback_data="feedback_wrong"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.effective_message.reply_text(result, reply_markup=reply_markup)

    # Screenshot olish
    if text.startswith("http"):
        try:
            screenshot = await asyncio.get_event_loop().run_in_executor(
                None, get_screenshot, text
            )
            if screenshot:
                await update.effective_message.reply_photo(
                    photo=screenshot,
                    caption="📸 Sayt ko'rinishi"
                )
        except:
            pass

async def feedback_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "feedback_correct":
        add_feedback("correct")
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text("✅ Rahmat! Fikringiz qabul qilindi.")
    elif query.data == "feedback_wrong":
        add_feedback("wrong")
        await query.edit_message_reply_markup(reply_markup=None)
        await query.message.reply_text("📝 Rahmat! Botni yaxshilash uchun foydalaniladi.")

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    name = update.effective_user.full_name
    add_user(user_id, name)

    message = update.effective_message
    if message.document:
        file = message.document
        filename = file.file_name or "unknown"
    elif message.photo:
        file = message.photo[-1]
        filename = "photo.jpg"
    elif message.video:
        file = message.video
        filename = file.file_name or "video.mp4"
    elif message.audio:
        file = message.audio
        filename = file.file_name or "audio.mp3"
    else:
        return

    await message.reply_text(f"📁 Fayl tekshirilmoqda: {filename}...")

    file_obj = await context.bot.get_file(file.file_id)
    file_bytes = await file_obj.download_as_bytearray()

    result = await asyncio.get_event_loop().run_in_executor(
        None, check_file, bytes(file_bytes), filename
    )

    await message.reply_text(result)