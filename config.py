from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", 19645327))
API_HASH = getenv("API_HASH", "92de937beb2f87db08df95bcca0ac2d6")

BOT_TOKEN = getenv("BOT_TOKEN", "6437907769:AAHGqmY8N3DU6cQIQ3YcNhTaGtU9UxgoAYA")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Tepthona:TepthonArabic@cluster0.dqmmh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

OWNER_ID = int(getenv("OWNER_ID", 1260465030))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Tepthon")
