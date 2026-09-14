import os
import random
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", "10000"))


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")

    def log_message(self, format, *args):
        pass


def start_server():
    server = ThreadingHTTPServer(("0.0.0.0", PORT), HealthHandler)
    server.serve_forever()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐔 أهلاً بك!\n\n"
        "اكتب /signal للحصول على إشارة تجريبية."
    )


async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    signal_value = random.choice([
        "1.20x",
        "1.50x",
        "2.00x",
        "2.50x"
    ])

    await update.message.reply_text(
        f"🐔 Chicken Road\n\n"
        f"📊 إشارة تجريبية: {signal_value}\n\n"
        "⚠️ هذه إشارة عشوائية للتجربة وليست توقعًا حقيقيًا."
    )


def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is not set")

    threading.Thread(target=start_server, daemon=True).start()

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
