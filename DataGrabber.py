import yfinance as yf

company = "IMBBY"

def convert_values(numbers_dict):

    converted_values = list()
    for item in numbers_dict:
        converted_values.append((item.year, item.value))

    return converted_values


def get_cashflow(ticker):
    '''Returns the net cashflow of the given ticker symbol for the last few years. Net cashflow is calculated from cash from operations and the capital expenditure.'''
    ticker = yf.Ticker(company)
    ticker_cashflow = ticker.cashflow
    ticker_cashflow= ticker_cashflow.to_dict('index')

    cash_from_op = ticker_cashflow["Total Cash From Operating Activities"]
    cap_ex = ticker_cashflow["Capital Expenditures"]
    #print(f"{company} Free Cashflow: ",cash_from_op)
    net_cashflow = dict()

    for item in cap_ex:
        net_cashflow[item] = cash_from_op[item] + cap_ex[item]
    return net_cashflow

cash = get_cashflow(company)

print(convert_values(cash))

