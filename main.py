import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text as TextFilter
import keyboard as kb
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from Vacations import direction
from reports import report
import about_company as ac
from support import BOT_SUPPORT

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
async def send_welcome(message: types.Message):
    await message.answer(
        "Бот, предоставяющий информацию о предприятии Северсталь.\n\nДля ознакомления с функциями "
        "нажмите на кнопку 'Помощь'",
        reply_markup=kb.markup1,
    )


@dp.message_handler(commands=["help"], state="*")
async def send_help(message):
    await message.answer("Sorry")


@dp.message_handler(TextFilter(equals=kb.financial_summary), state="*")
async def send_financial_summary(message: types.Message):
    await message.answer("Выберите раздел", reply_markup=kb.markupF)


@dp.message_handler(TextFilter(equals=kb.inf_about_report), state="*")
async def info_about_report(message: types.Message, state: FSMContext):
    await capital_or_report.choice.set()
    await message.answer("Выберите отчёт", reply_markup=kb.markup_of_report)


@dp.message_handler(
    lambda message: message.text
    in ["Общий доход компании", "Акционерный капитал", "Чистая прибыль"],
    state=capital_or_report.choice,
)
async def send_period(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["choice"] = message.text
    await capital_or_report.next()
    await message.answer("Выберите период", reply_markup=kb.markup_period)


@dp.message_handler(
    lambda message: message.text in ["Квартальный отчёт", "Годовой отчёт"],
    state=capital_or_report.period,
)
async def send_report(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["period"] = message.text
    await message.answer(
        report[data["choice"]][data["period"]], reply_markup=kb.markupF
    )


@dp.message_handler(TextFilter(equals=kb.stock), state="*")
async def send_stock(message: types.Message):
    from stock import stocks

    await message.answer(stocks())


@dp.message_handler(TextFilter(equals=kb.about_company), state="*")
async def send_info_about_campany(message: types.Message):
    await message.answer(ac.short_description, reply_markup=kb.markup_about_company)


@dp.message_handler(TextFilter(equals=kb.history), state="*")
async def send_history(message):
    from history import history_of_severstal

    await message.answer(history_of_severstal())


@dp.message_handler(TextFilter(equals=kb.the_structure_of_the_company), state="*")
async def send_structure(message: types.Message):
    await message.answer("Выберите раздел", reply_markup=kb.markup_structure)


@dp.message_handler(TextFilter(equals=kb.severstal_russian_steel), state="*")
async def send_structure(message: types.Message):
    await message.answer(
        ac.severstal_russian_steel, reply_markup=kb.markup_about_company
    )


@dp.message_handler(TextFilter(equals=kb.severstal_resource), state="*")
async def send_severstal_russian_steel(message: types.Message):
    await message.answer(ac.severstal_resource, reply_markup=kb.markup_about_company)


@dp.message_handler(TextFilter(equals=kb.key_assets), state="*")
async def send_key_assets(message: types.Message):
    await message.answer(ac.key_assets, reply_markup=kb.markup_about_company)


@dp.message_handler(TextFilter(equals=kb.trading_companies), state="*")
async def send_trading_companies(message: types.Message):
    await message.answer(ac.trading_companies, reply_markup=kb.markup_about_company)


@dp.message_handler(TextFilter(equals=kb.further_redistribution_enterprises), state="*")
async def send_further_redistribution_enterprises(message: types.Message):
    await message.answer(
        ac.further_redistribution_enterprises, reply_markup=kb.markup_about_company
    )


@dp.message_handler(TextFilter(equals=kb.other_businesses), state="*")
async def send_other_businesses(message: types.Message):
    await message.answer(ac.other_businesses, reply_markup=kb.markup_about_company)


@dp.message_handler(TextFilter(equals=kb.strategy_and_strategic_priorities), state="*")
async def send_strategy(message: types.Message):
    await message.answer(ac.startegy, reply_markup=kb.markup_about_company)


@dp.message_handler(TextFilter(equals=kb.leadership), state="*")
async def send_leadership(message: types.Message):
    await message.answer(
        "Выберите тип руководства", reply_markup=kb.markup_of_leadership
    )


@dp.message_handler(
    TextFilter(equals=kb.management_of_severstal_management_JSC), state="*"
)
async def send_management_of_severstal_management_JSC(message: types.Message):
    await message.answer(
        ac.management_of_severstal_management_JSC, reply_markup=kb.markup_about_company
    )


@dp.message_handler(TextFilter(equals=kb.enterprise_management), state="*")
async def send_enterprise_management(message: types.Message):
    await message.answer(ac.enterprise_management, reply_markup=kb.markup_about_company)


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


@dp.message_handler(TextFilter(equals=kb.back), state="*")
async def go_back(message: types.Message):
    await message.answer("Хорошо", reply_markup=kb.markup1)


@dp.message_handler()
async def send_help(message: types.Message, state="*"):
    await message.answer(BOT_SUPPORT())


@dp.message_handler()
async def send_error(message: types.Message, state='*'):
    await message.answer("Используйте навигационные кнопки!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
