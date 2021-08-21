import os

from aiogram import types

from data_b.dp_math import problem_translate_name


def get_inline_math_url():
    buttons = [
        types.InlineKeyboardButton(text="Хабр", url="https://habr.com/ru/post/207034/"),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def get_inline_math_formulas():
    buttons = [
        types.InlineKeyboardButton(text="Вывести подсказку", callback_data="hint_f"),
        types.InlineKeyboardButton(text="Вывести ответ", callback_data="answer_f")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)

    return keyboard


def get_inline_math_problems_category():
    buttons = []

    all_files_names = os.listdir(path="C:/Users/andrt/PycharmProjects/ConTia/data_b/json")

    for file_name in all_files_names:
        file_name = file_name.split('.json')[0]
        translated_name = problem_translate_name(file_name)
        buttons.append(types.InlineKeyboardButton(text=translated_name, callback_data=file_name))

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)

    return keyboard
