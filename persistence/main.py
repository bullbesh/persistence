"""Основной модуль проекта, объединяющий весь функционал бота
и выводящий информацию пользователю:
- Финансовые показатели
- О компании
- Вакансии
- Помощь
"""

import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text as TextFilter
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.markdown import bold

from . import about_company as ac
from . import keyboard as kb
from .history import severstal_history
from .reports import report
from .stock import stocks
from .support import BOT_SUPPORT
from .vacancies import direction


logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("TOKEN"))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class Vacancies(StatesGroup):
    """Состояние пользователя при ознакомлении с вакансиями предприятия.

    Пользователь выбирает направление вакансии, а потом город,
    после чего получает вакансии по данным критериям
    """

    vacation = State()
    city = State()


class Capitals(StatesGroup):
    """Состояние пользователя при ознакомлении с финансовой отчётностью компании.

    Пользователь может выбрать один из типов отчёта компании.
    После выбора типа отчёта нужно указать временной период
    """

    choice = State()
    period = State()


@dp.message_handler(commands=["start"], state="*")
async def send_welcome(message):
    """Отправка краткого описания бота."""
    await message.answer(
        "Бот, предоставяющий информацию о предприятии Северсталь.\n\n"
        "Для ознакомления с функциями нажмите на кнопку 'Помощь'",
        reply_markup=kb.markup1,
    )


@dp.message_handler(commands=["help"], state="*")
async def send_help(message):
    """Отправка помощи пользователю."""
    await message.answer("Sorry")


@dp.message_handler(TextFilter(equals=kb.FINANCIAL_PERFORMANCE), state="*")
async def send_financial_summary(message):
    """Отправка клавиатуры с следующими функциями:
    - Узнать стоимость акций компании
    - Финансовая отчётность компании
    """
    await message.answer("Выберите раздел", reply_markup=kb.finance_markup)


@dp.message_handler(TextFilter(equals=kb.FINANCIAL_STATEMENTS), state="*")
async def send_report_info(message, state):
    """Отправка финансового отчёта компании:
    - Общий доход компании
    - Акционерный капитал
    - Чистая прибыль
    """
    await Capitals.choice.set()
    await message.answer("Выберите отчёт", reply_markup=kb.report_markup)


@dp.message_handler(
    lambda message: message.text
    in ["Общий доход компании", "Акционерный капитал", "Чистая прибыль"],
    state=Capitals.choice,
)
async def send_period(message, state):
    """Отправка выбора между квартальным и годовым отчётами."""
    async with state.proxy() as data:
        data["choice"] = message.text
    await Capitals.next()
    await message.answer("Выберите период", reply_markup=kb.markup_period)


@dp.message_handler(
    lambda message: message.text in ["Квартальный отчёт", "Годовой отчёт"],
    state=Capitals.period,
)
async def send_report(message, state):
    """Отправка выбора между финансовой отчётностью
    компании и стоимостью акций.
    """
    async with state.proxy() as data:
        data["period"] = message.text
    await message.answer(
        report[data["choice"]][data["period"]], reply_markup=kb.finance_markup
    )


@dp.message_handler(TextFilter(equals=kb.BUTTON_STOCK_PRICE), state="*")
async def send_stock(message):
    """Отправка стоимости акций Северстали."""
    await message.answer(stocks())


@dp.message_handler(TextFilter(equals=kb.ABOUT_COMPANY), state="*")
async def send_company_info(message):
    """Отправка информации о Северстали, разбитой на разделы:
    - История компании
    - Структура компании
    - Стратегия и стратегические приоритеты
    - Руководство
    """
    await message.answer(
        ac.SHORT_DESCRIPTION,
        parse_mode=types.message.ParseMode.MARKDOWN,
        reply_markup=kb.company_markup,
    )


@dp.message_handler(TextFilter(equals=kb.COMPANY_HISTORY), state="*")
async def send_history(message):
    """Отправка истории компании."""
    await message.answer(severstal_history())


@dp.message_handler(TextFilter(equals=kb.COMPANY_STRUCTURE), state="*")
async def send_company_structure(message):
    """Отправка описания структуры компании."""
    await message.answer("Выберите раздел", reply_markup=kb.markup_structure)


@dp.message_handler(TextFilter(equals=kb.SEVERSTAL_RUSSIAN_STEEL), state="*")
async def send_severstal_russian_steel_structure(message):
    """Отправка информации о компании «Северсталь Российская сталь»."""
    await message.answer(
        ac.SEVERSTAL_RUSSIAN_STEEL, reply_markup=kb.company_markup
    )


@dp.message_handler(TextFilter(equals=kb.SEVERSTAL_RESOURCE), state="*")
async def send_severstal_russian_steel(message):
    """Отправка информации о компании «Северсталь Ресурс»."""
    await message.answer(ac.SEVERSTAL_RESOURCE, reply_markup=kb.company_markup)


@dp.message_handler(TextFilter(equals=kb.COMPANY_KEY_ASSETS), state="*")
async def send_key_assets(message):
    """Отправка информации о ключевых активах компании."""
    await message.answer(ac.COMPANY_KEY_ASSETS, reply_markup=kb.company_markup)


@dp.message_handler(TextFilter(equals=kb.TRADING_COMPANIES), state="*")
async def send_trading_companies(message):
    """Отправка информации о торговых компаниях."""
    await message.answer(ac.TRADING_COMPANIES, reply_markup=kb.company_markup)


@dp.message_handler(
    TextFilter(equals=kb.FURTHER_REDISTRIBUTION_ENTERPRISES), state="*"
)
async def send_further_redistribution_enterprises(message):
    """Отправка информации о предприятиях дальнейшего передела."""
    await message.answer(
        ac.FURTHER_REDISTRIBUTION_ENTERPRISES, reply_markup=kb.company_markup
    )


@dp.message_handler(TextFilter(equals=kb.OTHER_ENTERPRISES), state="*")
async def send_other_businesses(message):
    """Отправка информации о предприятиях,
    имеющих какое-либо отношение к Северстали.
    """
    await message.answer(ac.OTHER_ENTERPRISES, reply_markup=kb.company_markup)


@dp.message_handler(
    TextFilter(equals=kb.STRATEGY_AND_STRATEGIC_PRIORITIES), state="*"
)
async def send_strategy(message):
    """Отправка стратегии и стратегических приоритетов компании:
    - Стратегия устойчивого развития
    - Стратегические приоритеты «Северстали»
    """
    await message.answer(
        ac.COMPANY_STARTEGY,
        parse_mode=types.message.ParseMode.MARKDOWN,
        reply_markup=kb.company_markup,
    )


@dp.message_handler(TextFilter(equals=kb.COMPANY_LEADERSHIP), state="*")
async def send_leadership(message):
    """Отправка руководства предприятий, поделенного на три раздела:
    - Члены совета директоров
    - Руководство АО «Северсталь Менеджмент»
    - Руководство предприятий
    """
    await message.answer(
        "Выберите тип руководства", reply_markup=kb.leadership_markup
    )


@dp.message_handler(
    TextFilter(equals=kb.SEVERSTAL_MANAGEMENT_DIRECTION), state="*"
)
async def send_severstal_management_direction(message):
    """Отправка информации о руководстве АО «Северсталь Менеджмент»."""
    await message.answer(
        ac.SEVERSTAL_MANAGEMENT_DIRECTION, reply_markup=kb.company_markup
    )


@dp.message_handler(TextFilter(equals=kb.ENTERPRISE_MANAGEMENT), state="*")
async def send_enterprise_management(message):
    """Отправка информации о руководстве других предприятий."""
    await message.answer(
        ac.ENTERPRISE_MANAGEMENT, reply_markup=kb.company_markup
    )


@dp.message_handler(TextFilter(equals=kb.DIRECTORS_MEMBERS_BOARD), state="*")
async def send_board_members(message):
    """Отправка информации о членах совета директоров."""
    await message.answer(
        ac.DIRECTORS_MEMBERS_BOARD, reply_markup=kb.company_markup
    )


@dp.message_handler(TextFilter(equals=kb.BUTTON_VACANCIES), state="*")
async def send_direction(message):
    """Отправка информации о доступных на Северстали
    вакансиях, разбитой на разделы:
    - Произоводство
    - IT & Digital
    - Офис
    - Информация молодым специалистам)
    """
    await Vacancies.vacation.set()
    await message.answer("Выберите направление", reply_markup=kb.markup2)


@dp.message_handler(
    lambda message: message.text
    in ["Производство", "IT & Digital", "Офис", "Молодым специалистам"],
    state=Vacancies.vacation,
)
async def send_vacation(message, state):
    """Отправка выбора конкретного раздела с вакансиями и выбор города,
    в котором данное направление профдеятельности существует.
    """
    async with state.proxy() as data:
        data["vacation"] = message.text
    await Vacancies.next()
    await message.answer(
        "Выберите город", reply_markup=kb.keyboards[data["vacation"]]
    )


@dp.message_handler(
    lambda message: message.text in kb.CITIES_LIST, state=Vacancies.city
)
async def send_vactions(message, state):
    """Отправка вакансий по выбранным критериям - городу и направлению."""
    async with state.proxy() as data:
        data["city"] = message.text
    await message.answer(
        direction[data["vacation"]][data["city"]], reply_markup=kb.markup1
    )


@dp.message_handler(TextFilter(equals=kb.BUTTON_BACK), state="*")
async def go_back(message):
    """Отправка пользователя на ступень назад."""
    await message.answer("Хорошо", reply_markup=kb.markup1)


@dp.message_handler(TextFilter(equals=kb.BUTTON_HELP), state="*")
async def send_support(message, state="*"):
    """Отправка помощи пользователю.

    Отправляется объяснение принципа работы бота
    и краткое описание его функций
    """
    await message.answer(
        BOT_SUPPORT,
        parse_mode=types.message.ParseMode.MARKDOWN,
        reply_markup=kb.markup1,
    )


@dp.message_handler()
async def send_error(message, state="*"):
    """Обработка нераспознанного сообщения.

    В случае ввода пользователем сообщения,
    которое бот не сможет распознать, отправляется просьба
    по использованию навигационных кнопок
    """
    await message.answer(
        bold("Используйте навигационные кнопки!"),
        parse_mode=types.ParseMode.MARKDOWN_V2,
    )


def main():
    """Основная функция, отвечающая за запуск бота."""
    executor.start_polling(dp, skip_updates=True)
