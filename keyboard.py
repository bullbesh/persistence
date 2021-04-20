from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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
stock = "Узнать стоимсть акций Северстали"
history = "История Северстали"
helpp = "Помощь"
vac = "Вакансии"

manufacture = "Производство"
IT_and_Digital = "IT & Digital"
office = "Офис"
Young_professionals = "Молодым специалистам"
back = "Назад"

more1 = "Ещё"
more2 = "Больше"

btnStock = KeyboardButton(stock)
btnkb = KeyboardButton(history)
hlp = KeyboardButton(helpp)
btnV = KeyboardButton(vac)
markup1 = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(btnStock)
    .add(btnkb)
    .add(btnV)
    .add(hlp)
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

keyboards = {
    "Производство": markup3,
    "IT & Digital": markup4,
    "Офис": markup5,
    "Молодым специалистам": markup6,
}
