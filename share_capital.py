import investpy	

def quartely_capital():	
	balance_sheet = str(investpy.stocks.get_stock_financial_summary(stock='CHMF', country='Russia', summary_type='balance_sheet', period='quarterly')).split('\n')
	data = list()
	total_revenue = list()
	for value in balance_sheet[2:]:
		data.append(value.split()[0])
		total_revenue.append(value.split()[-1])
	return f'Общий доход компании за последние 4 года\n{data[-1]} - {total_revenue[-1]} млн. USD\n{data[2]} - \
	{total_revenue[2]} млн. USD\n{data[1]} - {total_revenue[1]} млн. USD\n{data[0]} - {total_revenue[0]} млн. USD'

def yearly_capital():	
	balance_sheet = str(investpy.stocks.get_stock_financial_summary(stock='CHMF', country='Russia', summary_type='balance_sheet', period='annual')).split('\n')
	data = list()
	total_revenue = list()
	for value in balance_sheet[2:]:
		data.append(value.split()[0])
		total_revenue.append(value.split()[-1])
	return f'Общий доход компании за последние 4 года\n{data[-1]} - {total_revenue[-1]} млн. USD\n{data[2]} - \
	{total_revenue[2]} млн. USD\n{data[1]} - {total_revenue[1]} млн. USD\n{data[0]} - {total_revenue[0]} млн. USD'

def yearly_net_income():
	net_income = str(investpy.stocks.get_stock_financial_summary(stock='CHMF', country='Russia', summary_type='income_statement ', period='annual')).split('\n')
	data = list()
	total_revenue = list()
	for value in net_income[2:]:
		data.append(value.split()[0])
		total_revenue.append(value.split()[4])
	return return f'Чистая прибыль компании за последние 4 года\n{data[-1]} - {total_revenue[-1]} млн. USD\n{data[2]} - \
	{total_revenue[2]} млн. USD\n{data[1]} - {total_revenue[1]} млн. USD\n{data[0]} - {total_revenue[0]} млн. USD'

def quartely_net_income():
	net_income = str(investpy.stocks.get_stock_financial_summary(stock='CHMF', country='Russia', summary_type='income_statement ', period='quarterly')).split('\n')
	data = list()
	total_revenue = list()
	for value in net_income[2:]:
		data.append(value.split()[0])
		total_revenue.append(value.split()[4])
	return return f'Чистая прибыль компании за последние 4 квартала\n{data[-1]} - {total_revenue[-1]} млн. USD\n{data[2]} - \
	{total_revenue[2]} млн. USD\n{data[1]} - {total_revenue[1]} млн. USD\n{data[0]} - {total_revenue[0]} млн. USD'