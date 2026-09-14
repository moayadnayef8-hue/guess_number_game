import os
import random
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐔 أهلاً بك!\n\n"
        "اكتب /signal للحصول على إشارة تجريبية."
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    signal_value = random.choice([
        "إشارة تجريبية: 1.20x",
        "إشارة تجريبية: 1.50x",
        "إشارة تجريبية: 2.00x",
        "إشارة تجريبية: 2.50x"
    ])

    await update.message.reply_text(
        f"🐔 Chicken Road\n\n"
        f"📊 {signal_value}\n\n"
        "⚠️ هذه إشارة عشوائية للتجربة وليست توقعًا حقيقيًا."
    )

def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is not set")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main() os
import random
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐔 أهلاً بك!\n\n"
        "اكتب /signal للحصول على إشارة تجريبية."
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    signal_value = random.choice([
        "إشارة تجريبية: 1.20x",
        "إشارة تجريبية: 1.50x",
        "إشارة تجريبية: 2.00x",
        "إشارة تجريبية: 2.50x"
    ])

    await update.message.reply_text(
        f"🐔 Chicken Road\n\n"
        f"📊 {signal_value}\n\n"
        "⚠️ هذه إشارة عشوائية للتجربة وليست توقعًا حقيقيًا."
    )

def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is not set")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
