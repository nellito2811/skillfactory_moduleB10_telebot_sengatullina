import  requests
import json
from config import keys


class APIExeption(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise APIExeption(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIExeption(f'Не удалось обработать валюту {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIExeption(f'Не удалось обработать валюту {base}.')        

        try:
            amount = float(amount.replace(",", "."))
        except ValueError:
            raise APIExeption(f'Не удалось обработать количество {amount}')
    
               
        
        url = (f"https://api.apilayer.com/exchangerates_data/convert?to={base_ticker}&from={quote_ticker}&amount={amount}")
        
        payload = {}
        headers= {
        "apikey": "0vhXB7bb29gh6Ab0aFn1HCm5TbmZuwXz"
        }

        r = requests.request("GET", url, headers=headers, data = payload)
        resp = json.loads(r.content)
        new_price = resp["result"]
        
        
        
        return new_price  
                

      