from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def choose_hand_btn():
    btn = InlineKeyboardMarkup()
    btn.add(
        InlineKeyboardButton("👊", callback_data="hand:stone"),
        InlineKeyboardButton("✌️", callback_data="hand:scissors"),
        InlineKeyboardButton("🤚", callback_data="hand:paper"),
    )

    return btn