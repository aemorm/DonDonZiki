import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.types import *
from keyboards import *
import random

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "6249459614:AAFZ-3TtE7ldtNcL2NB54lcES2N92wm8q10"

bot = Bot(token=BOT_TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot)

hands = ["stone", "scissors","paper"]
hands_emoji = {
    "stone": "👊",
    "scissors": "✌️",
    "paper": "🤚",
}
bot_choose = ''


@dp.message_handler(commands=['start'])
async def start_bot(message: Message):
    await message.answer("Salom men O`yin bot man.")


@dp.message_handler(commands=['game'])
async def start_game_bot(message: Message):
    global bot_choose
    btn = await choose_hand_btn()
    bot_choose = random.choice(hands)
    await message.answer("Tanlang: ", reply_markup=btn)


@dp.callback_query_handler(text_contains="hand:")
async def check_hands(call: CallbackQuery):
    user_choose = call.data.split(":")[1]
    # [hand, stone]
    # hand:stone

    if user_choose == bot_choose:
        await call.message.edit_text(f"Bir xil!\n\nBOT: {hands_emoji[bot_choose]}\nSIZ: {hands_emoji[user_choose]}")
    elif user_choose == 'stone':
        if bot_choose == 'scissors':
            await call.message.edit_text(f"Siz yutingiz!\n\nBOT: {hands_emoji[bot_choose]}\nSIZ: {hands_emoji[user_choose]}")
        else:
            await call.message.edit_text(f"Bot yuti!\n\nBOT: {hands_emoji[bot_choose]}\nSIZ: {hands_emoji[user_choose]}")

    elif user_choose == 'scissors':
        if bot_choose == 'paper':
            await call.message.edit_text(f"Siz yutingiz!\n\nBOT: {hands_emoji[bot_choose]}\nSIZ: {hands_emoji[user_choose]}")
        else:
            await call.message.edit_text(f"Bot yuti!\n\nBOT: {hands_emoji[bot_choose]}\nSIZ: {hands_emoji[user_choose]}")
    
    elif user_choose == 'paper':

        if bot_choose == 'stone':
            await call.message.edit_text(f"Siz yutingiz!\n\nBOT: {hands_emoji[bot_choose]}\nSIZ: {hands_emoji[user_choose]}")
        else:
            await call.message.edit_text(f"Bot yuti!\n\nBOT: {hands_emoji[bot_choose]}\nSIZ: {hands_emoji[user_choose]}")


if __name__ == "__main__":
    executor.start_polling(dp)






