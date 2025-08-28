import os
from dotenv import load_dotenv

load_dotenv()

# Quotex API
QX_EMAIL = os.getenv("QX_EMAIL")
QX_PASSWORD = os.getenv("QX_PASSWORD")
QX_LANG = "en"

# Telegram API
TG_API_ID = int(os.getenv("TG_API_ID"))
TG_API_HASH = os.getenv("TG_API_HASH")

# Bot Config Defaults
TRADE_PERCENT = 2   # percent of balance
