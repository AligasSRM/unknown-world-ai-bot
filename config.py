import os

# =========================
# UNKNOWN WORLD AI CONFIG
# =========================

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# AI
OPENAI_MODEL = os.getenv(
    "OPENAI_MODEL",
    "gpt-5.6-luna"
)

# Bot information
BOT_NAME = "UNKNOWN WORLD AI"
BOT_USERNAME = "@UnknownWorldAI73_bot"

# Free user limits
FREE_DAILY_MESSAGES = 30

# Application
PORT = int(os.getenv("PORT", "10000"))

# Environment
ENVIRONMENT = os.getenv(
    "ENVIRONMENT",
    "production"
)
