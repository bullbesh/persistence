import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text as TextFilter
import keyboard as kb
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from Vacations import direction
import os

token = os.getenv("TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class vaca(StatesGroup):
    vacation = State()
    city = State()


@dp.message_handler(commands=["start"], state="*")
async def send_welcome(message: types.Message):
    await message.answer(
        "Здравствуйте!!!\nЯ Северствль бот\nЧтобы ознакомиться с моими функциями на клавиатуре "
        "нажмите на кнопку 'Помощь'",
        reply_markup=kb.markup1,
    )


@dp.message_handler(commands=["help"], state="*")
async def send_help(message):
    await message.answer()


@dp.message_handler(TextFilter(equals=kb.stock), state="*")
async def send_stock(message: types.Message):
    from stock import stocks

    await message.answer(stocks())


@dp.message_handler(TextFilter(equals=kb.history), state="*")
async def send_history(message):
    from history import history_of_severstal

    await message.answer(history_of_severstal())


@dp.message_handler(TextFilter(equals=kb.vac), state="*")
async def send_direction(message):
    await vaca.vacation.set()
    await message.answer("Выберите направление", reply_markup=kb.markup2)


@dp.message_handler(
    lambda message: message.text
    in ["Производство", "IT & Digital", "Офис", "Молодым специалистам"],
    state=vaca.vacation,
)
async def send_vacationM(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["vacation"] = message.text
    await vaca.next()
    await message.answer("Выберите город", reply_markup=kb.keyboards[data["vacation"]])


@dp.message_handler(lambda message: message.text in kb.list1, state=vaca.city)
async def send_vactions(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["city"] = message.text

    await message.answer(
        direction[data["vacation"]][data["city"]], reply_markup=kb.markup1
    )


@dp.message_handler()
async def send_welcome(message):
    await message.answer("Воспользуйтесь, пожалуйста, клавиатурой")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
