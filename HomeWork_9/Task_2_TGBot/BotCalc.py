# Создать калькулятор для работы с рациональными и комплексными числами,
# организовать меню, добавив в неё систему логирования
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text('Если вы хотите воспользоваться калькулятором рациональных чисел,'
									'просто введите выражение')

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	await update.message.reply_text(eval(update.message.text))

app = ApplicationBuilder().token("5496383883:AAFP0l2Q149XAsA_ps3WurUIsS3f3ZbotgE").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("start", start))

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calc))

app.run_polling()
