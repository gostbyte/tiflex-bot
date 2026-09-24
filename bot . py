import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# PUT YOUR NEW TOKEN HERE AFTER YOU REVOKE
BOT_TOKEN = "8985397100:AAHnA4UoBePkwcuxmm36OmIpFKMwdaFmH44"
ADMIN_ID = 123456789 # Replace with your Telegram ID - get it from @userinfobot
CHANNEL_ID = -100xxxxxxxxxx # Your VIP Channel ID
INVITE_LINK = "https://t.me/+eZSf2nLG8U4wZTlk"
OPAY_NUMBER = "9120179122"
OPAY_NAME = "AKINOLA MUMIN FUNSHO"
PRICE = "7,000 NGN Monthly"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💳 Pay 7k Monthly", callback_data="pay")],
        [InlineKeyboardButton("✅ I Don Pay", callback_data="paid")]
    ]
    text = f"""
🔥 **TIFLEX TRADING SIGNALS VIP** 🔥

💰 Price: {PRICE}
📲 Pay to Opay:
`{OPAY_NUMBER}`
Name: {OPAY_NAME}

After payment, click "I Don Pay" and upload proof.
"""
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "pay":
        await query.message.reply_text(f"Send 7k to:\n\nOpay: `{OPAY_NUMBER}`\nName: {OPAY_NAME}\n\nThen click 'I Don Pay'", parse_mode="Markdown")

    elif query.data == "paid":
        await query.message.reply_text("Abeg upload your payment screenshot proof now 📸")

    elif query.data.startswith("approve_"):
        user_id = int(query.data.split("_")[1])
        try:
            # Approve join request
            await context.bot.approve_chat_join_request(chat_id=CHANNEL_ID, user_id=user_id)
            await context.bot.send_message(chat_id=user_id, text=f"✅ Payment confirmed! You have been approved to TIFLEX VIP.\n\nJoin here if you have not: {INVITE_LINK}")
            await query.edit_message_text(f"✅ Approved user {user_id}")
        except Exception as e:
            await query.edit_message_text(f"Approved, but user never requested to join yet. Send them link: {INVITE_LINK}\nError: {e}")

    elif query.data.startswith("reject_"):
        user_id = int(query.data.split("_")[1])
        await context.bot.send_message(chat_id=user_id, text="❌ Payment not confirmed. Please send correct proof or contact @tiflex_support")
        await query.edit_message_text(f"❌ Rejected user {user_id}")

async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    # Forward to Admin
    keyboard = [
        [InlineKeyboardButton("✅ Approve", callback_data=f"approve_{user.id}"),
         InlineKeyboardButton("❌ Reject", callback_data=f"reject_{user.id}")]
    ]
    await context.bot.forward_message(chat_id=ADMIN_ID, from_chat_id=update.effective_chat.id, message_id=update.message.message_id)
    await context.bot.send_message(chat_id=ADMIN_ID, text=f"New payment proof from @{user.username} ID: {user.id}\nName: {user.full_name}\n\nApprove to VIP?", reply_markup=InlineKeyboardMarkup(keyboard))
    await update.message.reply_text("✅ Proof received! Admin go check am now. You go get approval in few minutes.")

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))
app.add_handler(MessageHandler(filters.PHOTO, photo_handler))

app.run_polling()
