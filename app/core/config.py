from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
VIRUSTOTAL_API_KEY = os.getenv("VT_API_KEY")

ADMIN_ID = int(os.getenv("ADMIN_ID"))