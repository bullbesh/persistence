"""TODO: Сделать докстринг"""
from datetime import datetime, timedelta

import investpy


def stocks():
    """TODO: Сделать докстринг"""
    date_today = datetime.today().strftime("%d/%m/%Y")
    last_date = (datetime.today() - timedelta(days=5)).strftime("%d/%m/%Y")
    currently_date = datetime.today().strftime('%X')

    data = investpy.stocks.get_stock_historical_data(
        stock="CHMF",
        country="Russia",
        from_date=last_date,
        to_date=date_today,
        as_json=True,
    )
    conclusion = data["Close"]
    return f"{int(conclusion[3])} рублей стоит одна акция Северстали\n"
    f"Обновлено в {currently_date}"
