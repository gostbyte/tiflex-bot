import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("8985397100:AAHnA4UoBePkwcuxmm36OmIpFKMwdaFmH44")
CHANNEL_LINK = "https://t.me/+eZSf2nLG8U4wZTlk"

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

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
