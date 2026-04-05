from app.services.database import (
    init_db, db_add_user, db_get_users,
    db_add_check, db_add_feedback, db_get_stats
)

# Database ni ishga tushirish
init_db()

def add_user(user_id, name):
    db_add_user(user_id, name)

def add_check(result_type):
    db_add_check(result_type)

def add_feedback(feedback_type):
    db_add_feedback(feedback_type)

def get_stats():
    return db_get_stats()

def get_users():
    return db_get_users()

async def broadcast_message(context, text):
    users = db_get_users()
    count = 0
    for user in users:
        try:
            await context.bot.send_message(chat_id=user["id"], text=text)
            count += 1
        except:
            pass
    return count