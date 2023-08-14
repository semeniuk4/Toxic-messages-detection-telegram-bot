from aiogram import Dispatcher, Bot, types, executor
from config import TELEGRAM_BOT_TOKEN, DOCKER_API_URL
import requests
import logging

bot = Bot(token=TELEGRAM_BOT_TOKEN)

dp = Dispatcher(bot)

async def detect_toxic_message(message_text):
    response = requests.post(DOCKER_API_URL, json={'text': message_text})
    if response.status_code == 200:
        prediction = response.json()
        
        return prediction.get('result')
    else:
        return None


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.reply("Hello! I am Toxic Message Detector Bot.")

@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def handle_message(message: types.Message):
    user_input = message.text
    prediction = await detect_toxic_message(user_input)
    
    if prediction is None:
        await message.reply("Sorry, something went wrong while processing your message.")
    else:
        if prediction == 'Toxic Comment':
            await message.reply("Your message seems to be toxic. Please refrain from using offensive language.")
            try:
                await message.delete() 
            except Exception as e:
                logging.error(f"Error deleting message: {e}")
      
       