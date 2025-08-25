from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types
from openai import OpenAI

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

class Reference:
    """A class to store previously response from the OpenAI API"""
    def __init__(self) -> None:
        self.response = ""

reference = Reference()
model_name = "gpt-5"

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dispatcher = Dispatcher(bot)

def clear_past():
    """Clear previous conversation and context"""
    reference.response = ""

@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    clear_past()
    await message.reply("I've cleared the past conversation and context.")

@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply("Hi\nI am Jami Chat Bot! Created by Jami. How can I assist you?")

@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
    help_command = """
Hi There, I'm a Telegram bot created by Bappy! Please follow these commands:
    /start - to start the conversation
    /clear - to clear the past conversation and context
    /help - to get this help menu
I hope this helps.
    """
    await message.reply(help_command)

@dispatcher.message_handler()
async def chatgpt(message: types.Message):
    print("Bot starting...")
    print(f"Using token: {TELEGRAM_BOT_TOKEN[:5]}...")  # Debug: first 5 chars of token
    print(f">>> USER: \n\t{message.text}")

    # Call OpenAI ChatCompletion
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "assistant", "content": reference.response},
            {"role": "user", "content": message.text}
        ]
    )

    reply_text = response.choices[0].message.content
    reference.response = reply_text

    print(f">>> chatGPT: \n\t{reply_text}")
    await bot.send_message(chat_id=message.chat.id, text=reply_text)

if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=False)
    print("happy ending!")
