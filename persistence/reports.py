"""TODO: Сделать докстринг"""
import investpy


def yearly_report():
    """TODO: Сделать докстринг"""
    income_statement = investpy.stocks.get_stock_financial_summary(
        stock="CHMF",
        country="Russia",
        summary_type="income_statement",
        period="annual",
    )

    total_revenue = income_statement["Total Revenue"]
    conclusion = "Общий доход компании за последние 4 года\n"
    for i in range(4):
        conclusion += (
            f"{income_statement.index[i].strftime('%Y-%m-%d')} - "
            f"{total_revenue[i]} млн. USD\n"
        )
    return conclusion

def quarterly_report():
    """TODO: Сделать докстринг"""
    income_statement = investpy.stocks.get_stock_financial_summary(
        stock="CHMF",
        country="Russia",
        summary_type="income_statement",
        period="quarterly",
    )

    total_revenue = income_statement["Total Revenue"]
    conclusion = "Общий доход компании за последние 4 квартала\n"
    for i in range(4):
        conclusion += (
            f"{income_statement.index[i].strftime('%Y-%m-%d')} - "
            f"{total_revenue[i]} млн. USD\n"
        )
    return conclusion

def quarterly_capital():
    """TODO: Сделать докстринг"""
    balance_sheet = investpy.stocks.get_stock_financial_summary(
        stock="CHMF",
        country="Russia",
        summary_type="balance_sheet",
        period="quarterly",
    )

    total_revenue = balance_sheet["Total Assets"]
    conclusion = "Акционерный доход компании за последние 4 квартала\n"
    for i in range(4):
        conclusion += (
            f"{balance_sheet.index[i].strftime('%Y-%m-%d')} - "
            f"{total_revenue[i]} млн. USD\n"            
        )
    return conclusion


def yearly_capital():
    """TODO: Сделать докстринг"""
    balance_sheet = investpy.stocks.get_stock_financial_summary(
        stock="CHMF",
        country="Russia",
        summary_type="balance_sheet",
        period="annual",
    )

    total_revenue = balance_sheet["Total Assets"]
    conclusion = "Акционерный капитал компании за последние 4 года\n"
    for i in range(4):
        conclusion += (
            f"{balance_sheet.index[i].strftime('%Y-%m-%d')} - "
            f"{total_revenue[i]} млн. USD\n"            
        )
    return conclusion

def yearly_net_income():
    """TODO: Сделать докстринг"""
    net_income = investpy.stocks.get_stock_financial_summary(
        stock="CHMF",
        country="Russia",
        summary_type="income_statement",
        period="annual",
    )

    total_revenue = net_income["Total Revenue"]
    conclusion = "Чистая прибыль компании за последние 4 года\n"
    for i in range(4):
        conclusion += (
            f"{net_income.index[i].strftime('%Y-%m-%d')} - "
            f"{total_revenue[i]} млн. USD\n"            
        )
    return conclusion


def quarterly_net_income():
    """TODO: Сделать докстринг"""
    net_income = investpy.stocks.get_stock_financial_summary(
        stock="CHMF",
        country="Russia",
        summary_type="income_statement",
        period="quarterly",
    )

    total_revenue = net_income["Total Revenue"]
    conclusion = "Чистая прибыль компании за последние 4 квартала\n"
    for i in range(4):
        conclusion += (
            f"{net_income.index[i].strftime('%Y-%m-%d')} - "
            f"{total_revenue[i]} млн. USD\n"            
        )
    return conclusion


report = {
    "Общий доход компании": {
        "Квартальный отчёт": quarterly_report(),
        "Годовой отчёт": yearly_report(),
    },
    "Акционерный капитал": {
        "Квартальный отчёт": quarterly_capital(),
        "Годовой отчёт": yearly_capital(),
    },
    "Чистая прибыль": {
        "Квартальный отчёт": quarterly_net_income(),
        "Годовой отчёт": yearly_net_income(),
    },
}
