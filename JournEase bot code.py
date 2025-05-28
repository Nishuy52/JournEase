from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


TOKEN : Final = '7579183716:AAE5Qf5HLVuBergC26QFYInHt6JihrM0GFs'
BOT_USERNAME: Final = '@JournEaseBot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm JournEase, your journaling companion on Telegram.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm JournEase, your journaling companion on Telegram. " \
    "Here are the list of commands:\n\n/start- Initiates the bot \n\n/help - Provides the list of commands" \
    "\n\n/prompt - Gives you a prompt to get you started")

#Prompt command
import random 

# List of sample prompts
journal_prompts = [
    "📝 What was the best part of your day?",
    "🌧 What’s something that’s been on your mind lately?",
    "🌟 What’s a goal you’re working towards right now?",
    "📚 Write about a lesson you learned recently.",
    "❤️ Describe something or someone you're grateful for.",
    "💭 What’s a thought you can’t get out of your head today?",
]

async def prompt_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = random.choice(journal_prompts)
    await update.message.reply_text(f"Here’s your journaling prompt:\n\n{prompt}")


#User Journal Storage
user_journals = {}

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    message_text  = update.message.text

    if user_id not in user_journals:
        user_journals[user_id] = []
    
    user_journals[user_id].append(message_text)

    await update.message.reply_text("✅ Journal entry saved! Keep it up!")

# Bot Setup
def main():
    print("JournEase is running...")
    app = Application.builder().token(TOKEN).build()

    # Command handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("prompt", prompt_command))

    # Message handler for all text that isn’t a command
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start bot
    print("Polling...")
    app.run_polling(poll_interval=3)

# Run bot
if __name__  == '__main__':
    main()


