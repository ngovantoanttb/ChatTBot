import os

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from gpt import gpt_generate_image, gpt_generate_words, gpt_init

IS_USER_SELECTING_THEME = False


async def ping_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text("Pong!")


async def random_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    global IS_USER_SELECTING_THEME
    IS_USER_SELECTING_THEME = True
    await update.message.reply_text("Please select the theme")


async def handle_message(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    global IS_USER_SELECTING_THEME
    if IS_USER_SELECTING_THEME:
        IS_USER_SELECTING_THEME = False
        await update.message.reply_text(
            "Theme selected, wait for magic to happen"
        )
        theme = update.message.text

        cover_url = gpt_generate_image(theme)
        await update.message.reply_photo(cover_url)

        words = gpt_generate_words(theme)
        for item in words:
            await update.message.reply_markdown(
                f"*{item['word']}* - {item['description']}"
            )


async def handle_error(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(f"Error: {context.error}")


if __name__ == "__main__":
    telegram_bot_key = os.environ.get("TELEGRAM_BOT_KEY")
    if not telegram_bot_key:
        raise Exception("TELEGRAM_BOT_KEY is not set")

    app = ApplicationBuilder().token(telegram_bot_key).build()

    gpt_init()

    app.add_handler(CommandHandler("ping", ping_command))
    app.add_handler(CommandHandler("random", random_command))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_error_handler(handle_error)

    app.run_polling()
