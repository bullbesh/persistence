"""Модуль, содержащий в себе константы и клавиатуры, выводящиеся ботом через
файл main.py
"""

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


FINANCIAL_PERFORMANCE = "Финансовые показатели 📈"
QUARTELY_REPORT = "Квартальный отчёт"
YEARLY_REPORT = "Годовой отчёт"
TOTAL_COMPANY_INCOME = "Общий доход компании"
SHARE_CAPITAL = "Акционерный капитал"
NET_PROFIT = "Чистая прибыль"
FINANCIAL_STATEMENTS = "Финансовая отчётность компании"

ABOUT_COMPANY = "О компании 🏭"
COMPANY_HISTORY = "История компании"
COMPANY_STRUCTURE = "Структура компании"
STRATEGY_AND_STRATEGIC_PRIORITIES = "Стратегия и стратегические приоритеты"
COMPANY_LEADERSHIP = "Руководство"
SEVERSTAL_MANAGEMENT_DIRECTION = "Руководство АО «Северсталь Менеджмент»"
ENTERPRISE_MANAGEMENT = "Руководство предприятий"
DIRECTORS_MEMBERS_BOARD = "Члены совета директоров"

SEVERSTAL_RESOURCE = "«Северсталь Ресурс»"
SEVERSTAL_RUSSIAN_STEEL = "«Северсталь Российская сталь»"
COMPANY_KEY_ASSETS = "Ключевые активы"
TRADING_COMPANIES = "Торговые компании"
FURTHER_REDISTRIBUTION_ENTERPRISES = "Предприятия дальнейшего передела"
OTHER_ENTERPRISES = "Другие предприятия"

"""Города для поиска вакансий"""
CHEREPOVETS = "Череповец"
MOSCOW = "Москва"
SAINT_PETERSBURG = "Санкт-Петербург"
KOLPINO = "Колпино"
VORKUTA = "Воркута"
BELGOROD = "Белгород"
YAKOVLEVO = "Яковлево"
KOSTOMUKSHA = "Костомукша"
SHEKSNA = "Шексна"
STROITEL = "Строитель"
VORONEJ = "Воронеж"
SAMARA = "Самара"
YAROSLAVL = "Ярославль"
NIZHNY_NOVGOROD = "Нижний Новгород"
MURMANSK = "Мурманск"
KAZAN = "Казань"
NABEREZHNYE_CHELNY = "Набережные Челны"
BATAISK = "Батайск"
PODOLSK = "Подольск"
MOSSAN_LES_ALPILLES = "Моссан-лез-Альпий"
VOLGOGRAD = "Волгоград"
RED_SULIN = "Красный Сулин"
STUPINO = "Ступино"
TVER = "Тверь"

CITIES = [
    "Череповец",
    "Москва",
    "Санкт-Петербург",
    "Воркута",
    "Белгород",
    "Яковлево",
    "Костомукша",
    "Шексна",
    "Строитель",
    "Ярославль",
    "Воронеж",
    "Самара",
    "Колпино",
    "Нижний Новгород",
    "Мурманск",
    "Казань",
    "Набережные Челны",
    "Батайск",
    "Подольск",
    "Моссан-лез-Альпий",
    "Волгоград",
    "Красный Сулин",
    "Ступино",
    "Тверь",
]

BUTTON_STOCK_PRICE = "Узнать стоимость акций Северстали"
BUTTON_HELP = "Помощь ⚙️"
BUTTON_VACANCIES = "Вакансии 👨‍💼"

COMPANY_MANUFACTURE = "Производство"
COMPANY_IT_AND_DIGITAL = "IT & Digital"
COMPANY_OFFICE = "Офис"
COMPANY_YOUNG_PROFESSIONALS = "Молодым специалистам"
BUTTON_BACK = "Назад"

BUTTON_MORE1 = "Ещё"
BUTTON_MORE2 = "Больше"

"""Клавиатуры (...)"""
markup1 = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(FINANCIAL_PERFORMANCE))
    .add(KeyboardButton(ABOUT_COMPANY))
    .add(KeyboardButton(BUTTON_VACANCIES))
    .add(KeyboardButton(BUTTON_HELP))
)

finance_markup = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(BUTTON_STOCK_PRICE))
    .add(KeyboardButton(FINANCIAL_STATEMENTS))
    .add(KeyboardButton(BUTTON_BACK))
)

report_markup = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(TOTAL_COMPANY_INCOME))
    .add(KeyboardButton(SHARE_CAPITAL))
    .add(KeyboardButton(NET_PROFIT))
)

markup2 = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    .add(KeyboardButton(COMPANY_MANUFACTURE))
    .add(KeyboardButton(COMPANY_IT_AND_DIGITAL))
    .add(KeyboardButton(COMPANY_OFFICE))
    .add(KeyboardButton(COMPANY_YOUNG_PROFESSIONALS))
    .add(KeyboardButton(BUTTON_BACK))
)

markup3 = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .row(KeyboardButton(CHEREPOVETS), KeyboardButton(MOSCOW))
    .add(KeyboardButton(SAINT_PETERSBURG))
    .row(
        KeyboardButton(KOLPINO),
        KeyboardButton(VORKUTA),
        KeyboardButton(BELGOROD),
        KeyboardButton(YAKOVLEVO),
    )
    .row(
        KeyboardButton(KOSTOMUKSHA),
        KeyboardButton(SHEKSNA),
        KeyboardButton(STROITEL),
    )
)

markup4 = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    .row(
        KeyboardButton(KOLPINO),
        KeyboardButton(MOSCOW),
        KeyboardButton(BELGOROD),
    )
    .row(KeyboardButton(SAINT_PETERSBURG), KeyboardButton(KOSTOMUKSHA))
    .row(
        KeyboardButton(CHEREPOVETS),
        KeyboardButton(VORONEJ),
        KeyboardButton(YAROSLAVL),
    )
)

markup5 = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    .row(KeyboardButton(SAINT_PETERSBURG), KeyboardButton(MOSSAN_LES_ALPILLES))
    .row(
        KeyboardButton(MOSCOW),
        KeyboardButton(CHEREPOVETS),
        KeyboardButton(SAMARA),
        KeyboardButton(KOLPINO),
    )
    .row(
        KeyboardButton(YAROSLAVL),
        KeyboardButton(KAZAN),
        KeyboardButton(BATAISK),
        KeyboardButton(PODOLSK),
    )
    .row(
        KeyboardButton(VOLGOGRAD),
        KeyboardButton(VORONEJ),
        KeyboardButton(STUPINO),
        KeyboardButton(TVER),
    )
    .row(KeyboardButton(NIZHNY_NOVGOROD), KeyboardButton(RED_SULIN))
)

markup6 = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    .add(KeyboardButton(YAROSLAVL))
    .add(KeyboardButton(CHEREPOVETS))
)

markup_period = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(QUARTELY_REPORT))
    .add(KeyboardButton(YEARLY_REPORT))
)

company_markup = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(COMPANY_HISTORY))
    .add(KeyboardButton(COMPANY_STRUCTURE))
    .add(KeyboardButton(STRATEGY_AND_STRATEGIC_PRIORITIES))
    .add(KeyboardButton(COMPANY_LEADERSHIP))
    .add(KeyboardButton(BUTTON_BACK))
)

markup_structure = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(SEVERSTAL_RUSSIAN_STEEL))
    .add(KeyboardButton(SEVERSTAL_RESOURCE))
    .add(KeyboardButton(COMPANY_KEY_ASSETS))
    .add(KeyboardButton(TRADING_COMPANIES))
    .add(KeyboardButton(FURTHER_REDISTRIBUTION_ENTERPRISES))
    .add(KeyboardButton(OTHER_ENTERPRISES))
)

leadership_markup = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(DIRECTORS_MEMBERS_BOARD))
    .add(KeyboardButton(SEVERSTAL_MANAGEMENT_DIRECTION))
    .add(KeyboardButton(ENTERPRISE_MANAGEMENT))
)

keyboards = {
    "Производство": markup3,
    "IT & Digital": markup4,
    "Офис": markup5,
    "Молодым специалистам": markup6,
}
