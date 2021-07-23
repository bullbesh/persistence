from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

FINANCIAL_PERFORMANCE = "Финансовые показатели 📈"
QUARTELY_REPORT = "Квартальный отчёт"
YEARLY_REPORT = "Годовой отчёт"
TOTAL_COMPANY_INCOME = "Общий доход компании"
SHARE_CAPITAL = "Акционерный капитал"
NET_PROFIT = "Чистая прибыль"
FINANCIAL_STATEMENTS = "Финансовая отчётность компании"

ABOUT_COMPANY = "О компании 🏭"
HISTORY_OF_THE_COMPANY = "История компании"
STRUCTURE_OF_THE_COMPANY = "Структура компании"
STRATEGY_AND_STRATEGIC_PRIORITIES = "Стратегия и стратегические приоритеты"
LEADERSHIP_OF_THE_COMPANY = "Руководство"
DIRECTION_OF_SEVERSTAL_MANAGEMENT = "Руководство АО «Северсталь Менеджмент»"
ENTERPRISE_MANAGEMENT = "Руководство предприятий"
BOARD_OF_DIRECTORS_MEMBERS = "Члены совета директоров"

SEVERSTAL_RESOURCE = "«Северсталь Ресурс»"
SEVERSTAL_RUSSIAN_STEEL = "«Северсталь Российская сталь»"
KEY_ASSETS_OF_THE_COMPANY = "Ключевые активы"
TRADING_COMPANIES = "Торговые компании"
FURTHER_REDISTRIBUTION_ENTERPRISES = "Предприятия дальнейшего передела"
OTHER_ENTERPRISES = "Другие предприятия"

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

list1 = [
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

stock = "Узнать стоимость акций Северстали"
history = "История Северстали"
helpp = "Помощь ⚙️"
vac = "Вакансии 👨‍💼"

manufacture = "Производство"
IT_and_Digital = "IT & Digital"
office = "Офис"
Young_professionals = "Молодым специалистам"
back = "Назад"

more1 = "Ещё"
more2 = "Больше"

markup1 = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(FINANCIAL_PERFORMANCE))
    .add(KeyboardButton(ABOUT_COMPANY))
    .add(KeyboardButton(vac))
    .add(KeyboardButton(helpp))
)

markupF = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(stock))
    .add(KeyboardButton(FINANCIAL_STATEMENTS))
    .add(KeyboardButton(back))
)

markup_of_report = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(TOTAL_COMPANY_INCOME))
    .add(KeyboardButton(SHARE_CAPITAL))
    .add(KeyboardButton(NET_PROFIT))
)

markup2 = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    .add(KeyboardButton(manufacture))
    .add(KeyboardButton(IT_and_Digital))
    .add(KeyboardButton(office))
    .add(KeyboardButton(Young_professionals))
    .add(KeyboardButton(back))
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
    .row(KeyboardButton(KOSTOMUKSHA), KeyboardButton(SHEKSNA), KeyboardButton(STROUTEL))
)

markup4 = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    .row(KeyboardButton(KOLPINO), KeyboardButton(MOSCOW), KeyboardButton(BELGOROD))
    .row(KeyboardButton(SAINT_PETERSBURG), KeyboardButton(KOSTOMUKSHA))
    .row(KeyboardButton(CHEREPOVETS), KeyboardButton(VORONEJ), KeyboardButton(YAROSLAVL))
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

markup_ABOUT_COMPANY = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(HISTORY_OF_THE_COMPANY))
    .add(KeyboardButton(STRUCTURE_OF_THE_COMPANY))
    .add(KeyboardButton(STRATEGY_AND_STRATEGIC_PRIORITIES))
    .add(KeyboardButton(LEADERSHIP_OF_THE_COMPANY))
    .add(KeyboardButton(back))
)

markup_structure = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(SEVERSTAL_RUSSIAN_STEEL))
    .add(KeyboardButton(SEVERSTAL_RESOURCE))
    .add(KeyboardButton(KEY_ASSETS_OF_THE_COMPANY))
    .add(KeyboardButton(TRADING_COMPANIES))
    .add(KeyboardButton(FURTHER_REDISTRIBUTION_ENTERPRISES))
    .add(KeyboardButton(OTHER_ENTERPRISES))
)

markup_of_leadership = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(BOARD_OF_DIRECTORS_MEMBERS))
    .add(KeyboardButton(DIRECTION_OF_SEVERSTAL_MANAGEMENT))
    .add(KeyboardButton(ENTERPRISE_MANAGEMENT))

)

keyboards = {
    "Производство": markup3,
    "IT & Digital": markup4,
    "Офис": markup5,
    "Молодым специалистам": markup6,
}
