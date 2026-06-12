from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8915022707:AAFEgggZ259bjZk-8UnXc4ucWlUfCXQEXYw"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("جق به کام")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling(drop_pending_updates=True)