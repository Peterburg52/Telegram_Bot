from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_menu_keyboard(menu_level):
    keyboard = InlineKeyboardMarkup()
    for name in menu_level:
        if menu_level[name] is not None:
            keyboard.add(InlineKeyboardButton(name, callback_data=name))
    return keyboard