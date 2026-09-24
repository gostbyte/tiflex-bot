import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("I Have Paid - Send Proof", url="https://t.me/gostbyte")]]
    text = (
        "🔥 TIFLEX TRADING SIGNALS VIP 🔥\n\n"
        "💰 Price: 7,000 NGN Monthly\n"
        "💳 Pay to Opay: 9120179122\n"
        "Name: Tiflex\n\n"
        "After payment, click button below to send screenshot."
    )
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

def main():
    if not BOT_TOKEN:
        print("ERROR: BOT_TOKEN not set!")
        return
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot started - polling...")
    app.run_polling()

if __name__ == "__main__":
    main()
