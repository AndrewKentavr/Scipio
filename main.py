import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand

import middlewares
from config import BOT_TOKEN, ADMINS
import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from handlers.timer.timer_cycle import time_cycle
from handlers.register_cmd import reg_cmd

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)
scheduler = AsyncIOScheduler(timezone="Europe/Moscow")


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/cancel", description="Отмена действия"),
        BotCommand(command="/help", description="Просмотр функционала"),
        BotCommand(command="/math", description="Задания по математике"),
        BotCommand(command="/logic", description="Задания по логике"),
        BotCommand(command="/flashcard", description="Карточки для запомнинания"),
        BotCommand(command="/statistics", description="Просмотр статистики"),
        BotCommand(command="/timer", description="Таймер")
    ]
    await bot.set_my_commands(commands)


def timer_interval_func():
    """
    Функция управляющая таймером
    """
    scheduler.add_job(time_cycle, "interval", seconds=60, args=(dp,))


async def main():
    """
    middlewares.setup(dp) - запуск против флуда
    scheduler.start(), check_func() - запуск таймера и функция работающая с ним
    set_commands - назначает комманды бота
    reg_cmd - регистрация фсех необходимых функция
    """
    # Удаление последнего сообщения
    await bot.delete_webhook(drop_pending_updates=True)
    middlewares.setup(dp)

    scheduler.start()
    timer_interval_func()

    await set_commands(bot)
    # функция регистрации "register_message_handler"
    reg_cmd(dp)
    # await bot.send_message(ADMINS, "Bot - on", reply_markup=types.ReplyKeyboardRemove())

    # Запуск полинга
    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
