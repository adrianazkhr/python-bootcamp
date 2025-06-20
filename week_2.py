for num in range(10):
    print(f"{num}: Hello, world")

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
for idx in range(len(fruits)):
    print(fruits[idx])

students_cgpa = {
    'Rahman': 3.5,
    'Siti': 3.8,
    'Aniq': 3.2,
    'Sarah': 3.7,
    'Malik': 3.9,
    'John': 3.6,
    'Mary': 3.3,
    'Ali': 3.4,
    'Lisa': 3.1,
}
for key in students_cgpa:
    print(key, students_cgpa[key])
    print(key)
    print(students_cgpa['Rahman'])
for key, value in students_cgpa.items():
    print(key, value)

num =1
num = num + 1
num = num + 1
print(num)

num = 1
while num <= 5:
    print(num)
    num = num + 1

{
'company_name': 'ViewSoft',
'position': 'Software Engineer',
'pay': '$68K',
'pay_in_usd': 68000,
'pay_in_myr': 299200,
'income_class': 'high'
}

salaries = {
    "name": "Salaries Data for Software Engineer",
    "data": [
        {
            "company_name": "ViewSoft",
            "company_score": 4.8,
            "position": "Software Engineer",
            "location": "Manassas, VA",
            "pay": "$68K"
        },
        {
            "company_name": "KAIROS Inc",
            "company_score": 3.5,
            "position": "Software Engineer",
            "location": "Dahlgren, VA",
            "pay": "$6K"
        },
        
    ]
}
RATE = 4.4

for idx, item in enumerate(salaries['data']):
    pay_in_usd = item['pay'].replace('$', '').replace('K', '000')
    pay_in_usd = float(pay_in_usd)
    pay_in_myr = pay_in_usd * RATE
    item['pay_in_myr'] = pay_in_myr
    item['pay_in_usd'] = pay_in_usd
    
    if pay_in_usd < 100000:
        item['income_class'] = 'Low'
    elif pay_in_usd > 100000 and pay_in_usd < 200000:
        item['income_class'] = 'Middle'
    else:
        item['income_class'] = 'High'
    print(item)
    print('----')

import requests

data = requests.get('https://api.mybitx.com/api/1/ticker?pair=XRPMYR').json()
print(type(data))

import requests

data = requests.get('https://theedgemalaysia.com/api/loadMoreCategories?offset=0&categories=malaysia').json()
print(data)

import requests

LUNO_API = 'https://api.mybitx.com/api/1/ticker?pair=XRPMYR'
KUCOIN_API = 'https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=XRP-USDT'


price_in_luno = requests.get(LUNO_API).json()['last_trade']
price_in_kucoin = requests.get(KUCOIN_API).json()

print(price_in_kucoin)

import requests 

LUNO_API = 'https://api.mybitx.com/api/1/ticker?pair=XRPMYR'
KUCOIN_API = 'https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=XRP-USDT'
USD_MYR_RATE = 4.25



import requests

LUNO_API = 'https://api.mybitx.com/api/1/ticker?pair=XRPMYR'
KUCOIN_API = 'https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=XRP-USDT'


price_in_luno = float(requests.get(LUNO_API).json()['last_trade'])
price_in_kucoin = requests.get(KUCOIN_API).json()['data']['price']
price_in_kucoin_myr = float(price_in_kucoin) * USD_MYR_RATE


print(f"Price in Luno: {price_in_luno}, and price in Kucoin is {price_in_kucoin_myr}")
percentage_diff = (price_in_kucoin_myr - price_in_luno) / price_in_kucoin_myr * 100
print(f"The arbitrage opportunity between two are {percentage_diff:,.2f}")
