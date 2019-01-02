import quandl

def get_pricing_data(commodity, units):
    quandl.ApiConfig.api_key = 'i4-zCYgRx4KC4dUAFP_k'
    if commodity == 'gold':
        quandl_code = 'WGC/GOLD_DAILY_USD'
    elif commodity == 'silver':
        quandl_code = 'LBMA/SILVER'
    elif commodity == 'platinum':
        quandl_code = 'LPPM/PLAT'


    data = quandl.get(quandl_code, returns='numpy', rows=1)
    price =  float(data[0][1])
    extended_price = round(price * units, 2)
    skip_fee = 10.00
    setup_fee = 45.20
    monthly_price = round(extended_price / 12, 2)
    return {
        'price': '${:,.2f}'.format(price),
        'extended_price': '${:,.2f}'.format(extended_price),
        'skip_fee': '${:,.2f}'.format(skip_fee),
        'setup_fee': '${:,.2f}'.format(setup_fee),
        'monthly_price': '${:,.2f}'.format(monthly_price),
    }
