import investpy
from datetime import timedelta, datetime


def stocks():
    data_today = datetime.today().strftime("%d/%m/%Y")

    last_date = (datetime.today() - timedelta(days=5)).strftime("%d/%m/%Y")

    data = investpy.stocks.get_stock_historical_data(
        stock="CHMF",
        country="Russia",
        from_date=last_date,
        to_date=data_today,
        as_json=True,
    )
    return f"{((data.split())[-5])[:-1]} рублей стоит одна акция Северстали\nОбновлено в {(datetime.today()).strftime('%X')}"
