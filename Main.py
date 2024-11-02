from aiogram.filters import CommandStart, Command
from APIShaurma import GoAPI
import aiogram
import asyncio
import time

api_key = "7838160378:AAG7zhCo10s99GuCbf1oIm9tdxADgeXfIZA"

bot = aiogram.Bot(token=api_key)
dispatcher = aiogram.Dispatcher()

@dispatcher.message(CommandStart())
async def Start_cmd(message: aiogram.types.message):
    await message.answer("Hello shaur`men!")
    await message.answer("/help ?")

@dispatcher.message(Command('check_online'))
async def Start_cmd(message: aiogram.types.message):
    await message.answer("wait")
    result = GoAPI.GetData()
    await message.answer(result)

@dispatcher.message(Command('help'))
async def Start_cmd(message: aiogram.types.message):
    await message.answer("List commands:")
    await message.answer("/check_online")

async def main():
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")


