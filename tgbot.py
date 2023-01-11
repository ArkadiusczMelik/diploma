import requests
def binance_btc():
    resp = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    return resp.json()['price']
def binance_doge():
    resp = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=DOGEUSDT")
    return resp.json()['price']
def binance_etc():
    resp = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=ETCUSDT")
    return resp.json()['price']
def binance_dash():
    resp = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=DASHUSDT")
    return resp.json()['price']
def binance_augur():
    resp = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=REPUSDT")
    return resp.json()['price']
def binance_solana():
    resp = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT")
    return resp.json()['price']


def kraken_btc():
    resp = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSDT')
    return resp.json()['result']['XBTUSDT']['a'][0]
def kraken_doge():
    resp = requests.get('https://api.kraken.com/0/public/Ticker?pair=XDGUSDT')
    return resp.json()['result']['XDGUSDT']['a'][0]
def kraken_etc():
    resp = requests.get('https://api.kraken.com/0/public/Ticker?pair=XETCZUSD')
    return resp.json()['result']['XETCZUSD']['a'][0]
def kraken_dash():
    resp = requests.get('https://api.kraken.com/0/public/Ticker?pair=DASHUSD')
    return resp.json()['result']['DASHUSD']['a'][0]
def kraken_augur():
    resp = requests.get('https://api.kraken.com/0/public/Ticker?pair=XREPZUSD')
    return resp.json()['result']['XREPZUSD']['a'][0]
def kraken_solana():
    resp = requests.get('https://api.kraken.com/0/public/Ticker?pair=SOLUSDT')
    return resp.json()['result']['SOLUSDT']['a'][0]


def coinbase_btc():
    resp = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy')
    return resp.json()['data']['amount']
def coinbase_doge():
    resp = requests.get('https://api.coinbase.com/v2/prices/DOGE-USD/buy')
    return resp.json()['data']['amount']
def coinbase_etc():
    resp = requests.get('https://api.coinbase.com/v2/prices/ETC-USD/buy')
    return resp.json()['data']['amount']
def coinbase_dash():
    resp = requests.get('https://api.coinbase.com/v2/prices/DASH-USD/buy')
    return resp.json()['data']['amount']
def coinbase_augur():
    resp = requests.get('https://api.coinbase.com/v2/prices/REP-USD/buy')
    return resp.json()['data']['amount']
def coinbase_solana():
    resp = requests.get('https://api.coinbase.com/v2/prices/SOL-USD/buy')
    return resp.json()['data']['amount']


def kucoin_btc():
    resp = requests.get('https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT')
    return resp.json()['data']['price']
def kucoin_doge():
    resp = requests.get('https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=DOGE-USDT')
    return resp.json()['data']['price']
def kucoin_etc():
    resp = requests.get('https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=ETC-USDT')
    return resp.json()['data']['price']
def kucoin_dash():
    resp = requests.get('https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=DASH-USDT')
    return resp.json()['data']['price']
def kucoin_augur():
    resp = requests.get('https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=REP-USDT')
    return resp.json()['data']['price']
def kucoin_solana():
    resp = requests.get('https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=SOL-USDT')
    return resp.json()['data']['price']

binance_btc = float(binance_btc())
kraken_btc = float(kraken_btc())
coinbase_btc = float(coinbase_btc())
kucoin_btc = float(kucoin_btc())
binance_doge = float(binance_doge())
kraken_doge = float(kraken_doge())
coinbase_doge = float(coinbase_doge())
kucoin_doge = float(kucoin_doge())
binance_etc = float(binance_etc())
kraken_etc = float(kraken_etc())
coinbase_etc = float(coinbase_etc())
kucoin_etc = float(kucoin_etc())
binance_dash = float(binance_dash())
kraken_dash = float(kraken_dash())
coinbase_dash = float(coinbase_dash())
kucoin_dash = float(kucoin_dash())
binance_augur = float(binance_augur())
kraken_augur = float(kraken_augur())
coinbase_augur = float(coinbase_augur())
kucoin_augur = float(kucoin_augur())
binance_solana = float(binance_solana())
kraken_solana = float(kraken_solana())
coinbase_solana = float(coinbase_solana())
kucoin_solana = float(kucoin_solana())

