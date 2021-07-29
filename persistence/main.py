import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text as TextFilter
from aiogram.utils.markdown import bold, italic

from . import keyboard as kb
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from .vacancies import direction
from .reports import report
from . import about_company as ac
from .support import BOT_SUPPORT
from .stock import stocks
from .history import severstal_history


logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("TOKEN"))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class vaca(StatesGroup):
    vacation = State()
    city = State()


class capital_or_report(StatesGroup):
    choice = State()
    period = State()


@dp.message_handler(commands=["start"], state="*")
async def send_welcome(message):
    await message.answer(
        "Бот, предоставяющий информацию о предприятии Северсталь.\n\nДля ознакомления с функциями "
        "нажмите на кнопку 'Помощь'",
        reply_markup=kb.markup1,
    )


@dp.message_handler(commands=["help"], state="*")
async def send_help(message):
    await message.answer("Sorry")


@dp.message_handler(TextFilter(equals=kb.FINANCIAL_PERFORMANCE), state="*")
async def send_financial_summary(message):
    await message.answer("Выберите раздел", reply_markup=kb.markupF)


@dp.message_handler(TextFilter(equals=kb.FINANCIAL_STATEMENTS), state="*")
async def send_report_info(message, state):
    await capital_or_report.choice.set()
    await message.answer("Выберите отчёт", reply_markup=kb.report_markup)


@dp.message_handler(
    lambda message: message.text
    in ["Общий доход компании", "Акционерный капитал", "Чистая прибыль"],
    state=capital_or_report.choice,
)
async def send_period(message, state):
    async with state.proxy() as data:
        data["choice"] = message.text
    await capital_or_report.next()
    await message.answer("Выберите период", reply_markup=kb.markup_period)


@dp.message_handler(
    lambda message: message.text in ["Квартальный отчёт", "Годовой отчёт"],
    state=capital_or_report.period,
)
async def send_report(message, state):
    async with state.proxy() as data:
        data["period"] = message.text
    await message.answer(
        report[data["choice"]][data["period"]], reply_markup=kb.markupF
    )


@dp.message_handler(TextFilter(equals=kb.BUTTON_STOCK_PRICE), state="*")
async def send_stock(message):
    await message.answer(stocks())


@dp.message_handler(TextFilter(equals=kb.ABOUT_COMPANY), state="*")
async def send_company_info(message):
    await message.answer(ac.SHORT_DESCRIPTION, parse_mode=types.message.ParseMode.MARKDOWN, reply_markup=kb.company_markup)


@dp.message_handler(TextFilter(equals=kb.COMPANY_HISTORY), state="*")
async def send_history(message):
    await message.answer(severstal_history())


@dp.message_handler(TextFilter(equals=kb.COMPANY_STRUCTURE), state="*")
async def send_structure(message):
    await message.answer("Выберите раздел", reply_markup=kb.markup_structure)


@dp.message_handler(TextFilter(equals=kb.SEVERSTAL_RUSSIAN_STEEL), state="*")
async def send_structure(message):
    await message.answer(
        ac.SEVERSTAL_RUSSIAN_STEEL, reply_markup=kb.company_markup
    )


@dp.message_handler(TextFilter(equals=kb.SEVERSTAL_RESOURCE), state="*")
async def send_severstal_russian_steel(message):
    await message.answer(ac.SEVERSTAL_RESOURCE, reply_markup=kb.company_markup)


@dp.message_handler(TextFilter(equals=kb.COMPANY_KEY_ASSETS), state="*")
async def send_key_assets(message):
    await message.answer(ac.COMPANY_KEY_ASSETS, reply_markup=kb.company_markup)


@dp.message_handler(TextFilter(equals=kb.TRADING_COMPANIES), state="*")
async def send_trading_companies(message):
    await message.answer(ac.TRADING_COMPANIES, reply_markup=kb.company_markup)


@dp.message_handler(TextFilter(equals=kb.FURTHER_REDISTRIBUTION_ENTERPRISES), state="*")
async def send_further_redistribution_enterprises(message):
    await message.answer(
        ac.FURTHER_REDISTRIBUTION_ENTERPRISES, reply_markup=kb.company_markup
    )


@dp.message_handler(TextFilter(equals=kb.OTHER_ENTERPRISES), state="*")
async def send_other_businesses(message):
    await message.answer(ac.OTHER_ENTERPRISES, reply_markup=kb.company_markup)


@dp.message_handler(TextFilter(equals=kb.STRATEGY_AND_STRATEGIC_PRIORITIES), state="*")
async def send_strategy(message):
    await message.answer(ac.COMPANY_STARTEGY, parse_mode=types.message.ParseMode.MARKDOWN, reply_markup=kb.company_markup)


@dp.message_handler(TextFilter(equals=kb.COMPANY_LEADERSHIP), state="*")
async def send_leadership(message):
    await message.answer(
        "Выберите тип руководства", reply_markup=kb.leadership_markup
    )


@dp.message_handler(
    TextFilter(equals=kb.SEVERSTAL_MANAGEMENT_DIRECTION), state="*"
)
async def send_severstal_management_direction(message):
    await message.answer(
        ac.SEVERSTAL_MANAGEMENT_DIRECTION, reply_markup=kb.company_markup
    )


@dp.message_handler(TextFilter(equals=kb.ENTERPRISE_MANAGEMENT), state="*")
async def send_enterprise_management(message):
    await message.answer(ac.ENTERPRISE_MANAGEMENT, reply_markup=kb.company_markup)


@dp.message_handler(TextFilter(equals=kb.DIRECTORS_MEMBERS_BOARD), state='*')
async def send_board_members(message):
    await message.answer(ac.DIRECTORS_MEMBERS_BOARD, reply_markup=kb.company_markup)


@dp.message_handler(TextFilter(equals=kb.BUTTON_VACANCIES), state="*")
async def send_direction(message):
    await vaca.vacation.set()
    await message.answer("Выберите направление", reply_markup=kb.markup2)


@dp.message_handler(
    lambda message: message.text
    in ["Производство", "IT & Digital", "Офис", "Молодым специалистам"],
    state=vaca.vacation,
)
async def send_vacationM(message, state):
    async with state.proxy() as data:
        data["vacation"] = message.text
    await vaca.next()
    await message.answer("Выберите город", reply_markup=kb.keyboards[data["vacation"]])


@dp.message_handler(lambda message: message.text in kb.CITIES_LIST, state=vaca.city)
async def send_vactions(message, state):
    async with state.proxy() as data:
        data["city"] = message.text
    await message.answer(
        direction[data["vacation"]][data["city"]], reply_markup=kb.markup1
    )


@dp.message_handler(TextFilter(equals=kb.BUTTON_BACK), state="*")
async def go_back(message):
    await message.answer("Хорошо", reply_markup=kb.markup1)


@dp.message_handler(TextFilter(equals=kb.BUTTON_HELP), state="*")
async def send_help(message, state="*"):
    await message.answer(BOT_SUPPORT, parse_mode=types.message.ParseMode.MARKDOWN, reply_markup=kb.markup1)


@dp.message_handler()
async def send_error(message, state='*'):
    await message.answer(bold("Используйте навигационные кнопки!"), parse_mode=types.ParseMode.MARKDOWN_V2)


def main():
    executor.start_polling(dp, skip_updates=True)
