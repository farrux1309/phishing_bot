# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import ContextTypes
# from app.core.config import ADMIN_ID
# from app.services.stats import get_stats, get_users, broadcast_message

# def is_admin(user_id):
#     return user_id == ADMIN_ID

# async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.message.from_user.id

#     if not is_admin(user_id):
#         await update.message.reply_text("❌ Sizda ruxsat yo'q!")
#         return

#     stats = get_stats()
#     keyboard = [
#         [InlineKeyboardButton("📊 Statistika", callback_data="admin_stats")],
#         [InlineKeyboardButton("👥 Foydalanuvchilar", callback_data="admin_users")],
#         [InlineKeyboardButton("📢 Xabar yuborish", callback_data="admin_broadcast")],
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)

#     await update.message.reply_text(
#         f"👑 Admin Panel\n\n"
#         f"👥 Foydalanuvchilar: {stats['users']}\n"
#         f"🔗 Tekshirilgan linklar: {stats['total']}\n"
#         f"❌ Xavfli: {stats['malicious']}\n"
#         f"✅ Xavfsiz: {stats['safe']}\n",
#         reply_markup=reply_markup
#     )

# async def admin_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()
#     user_id = query.from_user.id

#     if not is_admin(user_id):
#         await query.edit_message_text("❌ Sizda ruxsat yo'q!")
#         return

#     if query.data == "admin_stats":
#         stats = get_stats()
#         await query.edit_message_text(
#             f"📊 Statistika\n\n"
#             f"👥 Foydalanuvchilar: {stats['users']}\n"
#             f"🔗 Jami tekshirilgan: {stats['total']}\n"
#             f"❌ Xavfli: {stats['malicious']}\n"
#             f"⚠️ Shubhali: {stats['suspicious']}\n"
#             f"✅ Xavfsiz: {stats['safe']}\n"
#         )

#     elif query.data == "admin_users":
#         users = get_users()
#         if not users:
#             await query.edit_message_text("👥 Hali foydalanuvchi yo'q.")
#             return
#         text = "👥 Foydalanuvchilar:\n\n"
#         for u in users[:20]:
#             text += f"• {u['name']} (ID: {u['id']})\n"
#         await query.edit_message_text(text)

#     elif query.data == "admin_broadcast":
#         await query.edit_message_text(
#             "📢 Barcha foydalanuvchilarga xabar yuboring:\n\n"
#             "/broadcast Xabar matni"
#         )

# async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.message.from_user.id

#     if not is_admin(user_id):
#         await update.message.reply_text("❌ Sizda ruxsat yo'q!")
#         return

#     if not context.args:
#         await update.message.reply_text("❌ Xabar matni kiriting!\nMasalan: /broadcast Salom!")
#         return

#     text = " ".join(context.args)
#     count = await broadcast_message(context, text)
#     await update.message.reply_text(f"✅ Xabar {count} ta foydalanuvchiga yuborildi!")
    
    
    
    
    
    
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from app.core.config import ADMIN_ID
from app.services.stats import get_stats, get_users, broadcast_message

def is_admin(user_id):
    return user_id == ADMIN_ID

async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id

    if not is_admin(user_id):
        await update.message.reply_text("❌ Sizda ruxsat yo'q!")
        return

    stats = get_stats()
    total_feedback = stats["feedback_correct"] + stats["feedback_wrong"]
    accuracy = round(stats["feedback_correct"] / total_feedback * 100) if total_feedback > 0 else 0

    keyboard = [
        [InlineKeyboardButton("📊 Statistika", callback_data="admin_stats")],
        [InlineKeyboardButton("👥 Foydalanuvchilar", callback_data="admin_users")],
        [InlineKeyboardButton("📢 Xabar yuborish", callback_data="admin_broadcast")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"👑 Admin Panel\n\n"
        f"👥 Foydalanuvchilar: {stats['users']}\n"
        f"🔗 Tekshirilgan linklar: {stats['total']}\n"
        f"❌ Xavfli: {stats['malicious']}\n"
        f"✅ Xavfsiz: {stats['safe']}\n\n"
        f"👍 To'g'ri feedback: {stats['feedback_correct']}\n"
        f"👎 Noto'g'ri feedback: {stats['feedback_wrong']}\n"
        f"🎯 Aniqlik: {accuracy}%",
        reply_markup=reply_markup
    )

async def admin_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    if not is_admin(user_id):
        await query.edit_message_text("❌ Sizda ruxsat yo'q!")
        return

    if query.data == "admin_stats":
        stats = get_stats()
        total_feedback = stats["feedback_correct"] + stats["feedback_wrong"]
        accuracy = round(stats["feedback_correct"] / total_feedback * 100) if total_feedback > 0 else 0

        await query.edit_message_text(
            f"📊 Statistika\n\n"
            f"👥 Foydalanuvchilar: {stats['users']}\n"
            f"🔗 Jami tekshirilgan: {stats['total']}\n"
            f"❌ Xavfli: {stats['malicious']}\n"
            f"⚠️ Shubhali: {stats['suspicious']}\n"
            f"✅ Xavfsiz: {stats['safe']}\n\n"
            f"👍 To'g'ri feedback: {stats['feedback_correct']}\n"
            f"👎 Noto'g'ri feedback: {stats['feedback_wrong']}\n"
            f"🎯 Aniqlik: {accuracy}%"
        )

    elif query.data == "admin_users":
        users = get_users()
        if not users:
            await query.edit_message_text("👥 Hali foydalanuvchi yo'q.")
            return
        text = "👥 Foydalanuvchilar:\n\n"
        for u in users[:20]:
            text += f"• {u['name']} (ID: {u['id']})\n"
        await query.edit_message_text(text)

    elif query.data == "admin_broadcast":
        await query.edit_message_text(
            "📢 Barcha foydalanuvchilarga xabar yuboring:\n\n"
            "/broadcast Xabar matni"
        )

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id

    if not is_admin(user_id):
        await update.message.reply_text("❌ Sizda ruxsat yo'q!")
        return

    if not context.args:
        await update.message.reply_text("❌ Xabar matni kiriting!\nMasalan: /broadcast Salom!")
        return

    text = " ".join(context.args)
    count = await broadcast_message(context, text)
    await update.message.reply_text(f"✅ Xabar {count} ta foydalanuvchiga yuborildi!")