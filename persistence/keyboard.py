from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

financial_summary = "Финансовые показатели 📈"
quartely_report = "Квартальный отчёт"
yearly_report = "Годовой отчёт"
total_company_income = "Общий доход компании"
share_capital = "Акционерный капитал"
net_income = "Чистая прибыль"
inf_about_report = "Финансовая отчётность компании"

about_company = "О компании 🏭"
history = "История компании"
the_structure_of_the_company = "Структура компании"
strategy_and_strategic_priorities = "Стратегия и стратегические приоритеты"
leadership = "Руководство"
management_of_severstal_management_JSC = "Руководство АО «Северсталь Менеджмент»"
enterprise_management = "Руководство предприятий"
board_members = "Члены совета директоров"

severstal_resource = "«Северсталь Ресурс»"
severstal_russian_steel = "«Северсталь Российская сталь»"
key_assets = "Ключевые активы"
trading_companies = "Торговые компании"
further_redistribution_enterprises = "Предприятия дальнейшего передела"
other_businesses = "Другие предприятия"

cherep = "Череповец"
moscow = "Москва"
peter = "Санкт-Петербург"
kolpino = "Колпино"
vorkuta = "Воркута"
belgorod = "Белгород"
yakov = "Яковлево"
kosto = "Костомукша"
milk = "Шексна"
work = "Строитель"
voron = "Воронеж"
sam = "Самара"
yarik = "Ярославль"
nn = "Нижний Новгород"
mm = "Мурманск"
kaz = "Казань"
nab_chel = "Набережные Челны"
bat = "Батайск"
pod = "Подольск"
mla = "Моссан-лез-Альпий"
volgograd = "Волгоград"
red_sul = "Красный Сулин"
stupino = "Ступино"
Tver = "Тверь"
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
    .add(KeyboardButton(financial_summary))
    .add(KeyboardButton(about_company))
    .add(KeyboardButton(vac))
    .add(KeyboardButton(helpp))
)

markupF = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(stock))
    .add(KeyboardButton(inf_about_report))
    .add(KeyboardButton(back))
)

markup_of_report = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(total_company_income))
    .add(KeyboardButton(share_capital))
    .add(KeyboardButton(net_income))
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
    .row(KeyboardButton(cherep), KeyboardButton(moscow))
    .add(KeyboardButton(peter))
    .row(
        KeyboardButton(kolpino),
        KeyboardButton(vorkuta),
        KeyboardButton(belgorod),
        KeyboardButton(yakov),
    )
    .row(KeyboardButton(kosto), KeyboardButton(milk), KeyboardButton(work))
)

markup4 = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    .row(KeyboardButton(kolpino), KeyboardButton(moscow), KeyboardButton(belgorod))
    .row(KeyboardButton(peter), KeyboardButton(kosto))
    .row(KeyboardButton(cherep), KeyboardButton(voron), KeyboardButton(yarik))
)

markup5 = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    .row(KeyboardButton(peter), KeyboardButton(mla))
    .row(
        KeyboardButton(moscow),
        KeyboardButton(cherep),
        KeyboardButton(sam),
        KeyboardButton(kolpino),
    )
    .row(
        KeyboardButton(yarik),
        KeyboardButton(kaz),
        KeyboardButton(bat),
        KeyboardButton(pod),
    )
    .row(
        KeyboardButton(volgograd),
        KeyboardButton(voron),
        KeyboardButton(stupino),
        KeyboardButton(Tver),
    )
    .row(KeyboardButton(nn), KeyboardButton(red_sul))
)

markup6 = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    .add(KeyboardButton(yarik))
    .add(KeyboardButton(cherep))
)

markup_period = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(quartely_report))
    .add(KeyboardButton(yearly_report))
)

markup_about_company = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(history))
    .add(KeyboardButton(the_structure_of_the_company))
    .add(KeyboardButton(strategy_and_strategic_priorities))
    .add(KeyboardButton(leadership))
    .add(KeyboardButton(back))
)

markup_structure = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(severstal_russian_steel))
    .add(KeyboardButton(severstal_resource))
    .add(KeyboardButton(key_assets))
    .add(KeyboardButton(trading_companies))
    .add(KeyboardButton(further_redistribution_enterprises))
    .add(KeyboardButton(other_businesses))
)

markup_of_leadership = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(board_members))
    .add(KeyboardButton(management_of_severstal_management_JSC))
    .add(KeyboardButton(enterprise_management))

)

keyboards = {
    "Производство": markup3,
    "IT & Digital": markup4,
    "Офис": markup5,
    "Молодым специалистам": markup6,
}
