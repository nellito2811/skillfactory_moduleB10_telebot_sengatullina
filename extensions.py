import  requests
import json
from config import keys


class ConvertionExeption(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionExeption(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {base}.')        

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'Не удалось обработать количество {amount}')
    
        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={base_ticker}&symbols={quote_ticker}')
        resp = json.loads(r.content)
        print(resp)
        new_price = resp['rates'][quote_ticker] * amount
        
        
        # url = f"https://api.apilayer.com/exchangerates_data/convert?to={quote_ticker}&from={base_ticker}&amount={amount}"
        
        # payload = {}
        # headers= {
        # "apikey": "0vhXB7bb29gh6Ab0aFn1HCm5TbmZuwXz"
        # }

        # r = requests.request("GET", url, headers=headers, data = payload)
        # resp = json.loads(r.content)
        # new_price = resp[result][total] * amount
        
        
        
        return new_price  
                

      