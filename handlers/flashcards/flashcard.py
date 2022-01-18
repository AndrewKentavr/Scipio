from aiogram import types, Dispatcher

from handlers.keyboards.default import flashcard_menu


async def flashcard_start(message: types.Message):
    await message.answer('При нажатии на кнопку "Начать учить карточки" начнется процесс тренировки с карточками')
    await message.answer('При нажатии на кнопку "Управление карточками" вы перейдете в раздел для изменения карточек',
                         reply_markup=flashcard_menu.get_keyboard_flashcard_start())


def register_handlers_flashcard(dp: Dispatcher):
    dp.register_message_handler(flashcard_start, commands='flashcard', state="*")
