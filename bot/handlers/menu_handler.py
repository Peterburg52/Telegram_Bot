from aiogram import Router, types
from aiogram.types import CallbackQuery
from ..config.menu_config import MENU_STRUCTURE  # Исправленный импорт
from bot.keyboards.menu import create_menu_keyboard

router = Router()

@router.message()
async def show_main_menu(message: types.Message):
    await message.answer("Выберите категорию:", reply_markup=create_menu_keyboard(MENU_STRUCTURE))

@router.callback_query()
async def navigate_menu(callback: CallbackQuery):
    menu_path = callback.data.split(" > ")
    current_menu = MENU_STRUCTURE

    for level in menu_path:
        current_menu = current_menu.get(level, {})

    if isinstance(current_menu, dict):
        await callback.message.edit_text(f"Выберите категорию: {callback.data}",
                                         reply_markup=create_menu_keyboard(current_menu))
    else:
        await callback.message.answer_photo(photo=current_menu["image"], caption=current_menu["description"])