# # from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, CallbackQueryHandler, filters
# # from app.bot.handlers import start, help_command, lang_command, lang_callback, handle_message
# # from app.core.config import BOT_TOKEN

# # def main():
# #     app = ApplicationBuilder().token(BOT_TOKEN).build()
# #     app.add_handler(CommandHandler("start", start))
# #     app.add_handler(CommandHandler("help", help_command))
# #     app.add_handler(CommandHandler("lang", lang_command))
# #     app.add_handler(CallbackQueryHandler(lang_callback, pattern="^lang_"))
# #     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
# #     print("Bot ishga tushdi 🚀")
# #     app.run_polling()

# # if __name__ == "__main__":
# #     main()


# # from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, CallbackQueryHandler, filters
# # from app.bot.handlers import start, help_command, lang_command, lang_callback, handle_message
# # from app.bot.admin import admin_panel, admin_callback, broadcast
# # from app.core.config import BOT_TOKEN

# # def main():
# #     app = ApplicationBuilder().token(BOT_TOKEN).build()
# #     app.add_handler(CommandHandler("start", start))
# #     app.add_handler(CommandHandler("help", help_command))
# #     app.add_handler(CommandHandler("lang", lang_command))
# #     app.add_handler(CommandHandler("admin", admin_panel))
# #     app.add_handler(CommandHandler("broadcast", broadcast))
# #     app.add_handler(CallbackQueryHandler(lang_callback, pattern="^lang_"))
# #     app.add_handler(CallbackQueryHandler(admin_callback, pattern="^admin_"))
# #     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
# #     print("Bot ishga tushdi 🚀")
# #     app.run_polling()

# # if __name__ == "__main__":
# #     main()


# from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, CallbackQueryHandler, filters
# from app.bot.handlers import start, help_command, lang_command, lang_callback, handle_message, handle_file
# from app.bot.admin import admin_panel, admin_callback, broadcast
# from app.core.config import BOT_TOKEN

# def main():
#     app = ApplicationBuilder().token(BOT_TOKEN).build()
#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CommandHandler("help", help_command))
#     app.add_handler(CommandHandler("lang", lang_command))
#     app.add_handler(CommandHandler("admin", admin_panel))
#     app.add_handler(CommandHandler("broadcast", broadcast))
#     app.add_handler(CallbackQueryHandler(lang_callback, pattern="^lang_"))
#     app.add_handler(CallbackQueryHandler(admin_callback, pattern="^admin_"))
#     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
#     app.add_handler(MessageHandler(
#         filters.Document.ALL | filters.PHOTO | filters.VIDEO | filters.AUDIO,
#         handle_file
#     ))
#     print("Bot ishga tushdi 🚀")
#     app.run_polling()

# if __name__ == "__main__":
#     main()


from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, CallbackQueryHandler, filters
from app.bot.handlers import start, help_command, lang_command, lang_callback, handle_message, handle_file, feedback_callback, join_callback
from app.bot.admin import admin_panel, admin_callback, broadcast
from app.core.config import BOT_TOKEN

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("lang", lang_command))
    app.add_handler(CommandHandler("admin", admin_panel))
    app.add_handler(CommandHandler("broadcast", broadcast))
    app.add_handler(CallbackQueryHandler(join_callback, pattern="^join$"))
    app.add_handler(CallbackQueryHandler(lang_callback, pattern="^lang_"))
    app.add_handler(CallbackQueryHandler(admin_callback, pattern="^admin_"))
    app.add_handler(CallbackQueryHandler(feedback_callback, pattern="^feedback_"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(MessageHandler(
        filters.Document.ALL | filters.PHOTO | filters.VIDEO | filters.AUDIO,
        handle_file
    ))
    print("Bot ishga tushdi 🚀")
    app.run_polling()

if __name__ == "__main__":
    main()