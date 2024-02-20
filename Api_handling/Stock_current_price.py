import requests

def stock_price(stock_symbol):
    uri = f'https://api.freeapi.app/api/v1/public/stocks/{stock_symbol}'
    response = requests.get(uri).json()
    
    if response['statusCode'] == 200 and 'data' in response:
        data = response['data']
        stock_name = data['Name']
        stock_current_price = data['CurrentPrice']
        return stock_name, stock_current_price
    else:
        raise Exception('Failed to fetch from the api')


def main():
    try:
        symbol = input('Enter your stock symbol ').upper()
        stock_name, stock_current_price = stock_price(stock_symbol=symbol)
        print(f'Name of the stock is {stock_name}\nCurrent price is {stock_current_price}')
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()