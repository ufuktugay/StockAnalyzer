import yfinance as yf

company = "MSFT"
'''
Returns the net cashflow of the given ticker symbol for the last few years. Net cashflow is calculated from cash from operations and the capital expenditure.
'''
def get_cashflow(ticker):
    ticker = yf.Ticker(company)
    ticker_cashflow = ticker.cashflow

    ticker_cashflow= ticker_cashflow.to_dict('index')

    cash_from_op = ticker_cashflow["Total Cash From Operating Activities"]
    cap_ex = ticker_cashflow["Capital Expenditures"]
    print(cash_from_op, "\n")
    net_cashflow = dict()

    for item in cap_ex:
        net_cashflow[item] = cash_from_op[item] + cap_ex[item]
        print(net_cashflow)
    
    return net_cashflow

get_cashflow(company)