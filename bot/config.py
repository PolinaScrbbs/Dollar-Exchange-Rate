from dotenv import load_dotenv
import os

os.environ.pop("BOT_TOKEN", None)
os.environ.pop("CURRENCY_API_URL", None)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CURRENCY_API_URL = os.getenv("CURRENCY_API_URL")
