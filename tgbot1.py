import telebot
from telebot import types
import time
from datetime import datetime
import requests



bot=telebot.TeleBot('5973909126:AAEwzEf-hiDPaHeSGK04mFMAlrPPDYhCRxY')

@bot.message_handler(commands=['start', 'go'])
def start(message):
    if message.text == '/start':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1=types.KeyboardButton("By exchange(Биржа)")
        item2=types.KeyboardButton("By cryptocurrency")
        markup.add(item1, item2)
        bot.send_message(message.from_user.id, "Hi, this is the bot-converter of currency in real time. Choose by which criteria do you want see information?", reply_markup=markup);
        bot.register_next_step_handler(message, start1);
    else:
        bot.send_message(message.from_user.id, 'Type /start');

def start1(message):
    choose = message.text
    print(choose)
    if (choose=="By exchange(Биржа)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        item1=types.KeyboardButton("Binance")
        item2=types.KeyboardButton("Coinbase")
        item3=types.KeyboardButton("Kraken")
        item4=types.KeyboardButton("KuCoin")
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.from_user.id, "Choose which cryptocurrency exchange you are interested in?", reply_markup=markup);
        bot.register_next_step_handler(message, exchange);
    elif (choose == "By cryptocurrency"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1=types.KeyboardButton("DogeCoin")
        item2=types.KeyboardButton("Bitcoin")
        item3=types.KeyboardButton("Etherium")
        item4=types.KeyboardButton("DASH")
        item5=types.KeyboardButton("Augur")
        item6=types.KeyboardButton("Solana")
        markup.add(item1, item2, item3, item4, item5, item6)
        bot.send_message(message.from_user.id, "Choose what currency you are interested in?", reply_markup=markup);
        bot.register_next_step_handler(message, crypto1);
    else:
        bot.send_message(message.from_user.id, "Choose from menu please")
        bot.register_next_step_handler(message, start);

def exchange(message):
    exchange = message.text
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

    if exchange == 'Binance':
        bot.send_message(message.from_user.id, 'Wait please...')
        binance_btc = float(binance_btc())
        binance_doge = float(binance_doge())
        binance_etc = float(binance_etc())
        binance_dash = float(binance_dash())
        binance_augur = float(binance_augur())
        binance_solana = float(binance_solana())
        bot.send_message(message.from_user.id, f'1 DOGE = {binance_doge} USDT \n1 BTC = {binance_btc} USDT \n1 ETC = {binance_etc} USDT \n1 DASH = {binance_dash} USDT \n1 REP = {binance_augur} USDT \n1 SOL = {binance_solana} USDT');
        bot.send_message(message.from_user.id, 'If you want to know more, type /start');
    elif exchange == 'Coinbase':
        bot.send_message(message.from_user.id, 'Wait please...')
        coinbase_btc = float(coinbase_btc())
        coinbase_doge = float(coinbase_doge())
        coinbase_etc = float(coinbase_etc())
        coinbase_dash = float(coinbase_dash())
        coinbase_augur = float(coinbase_augur())
        coinbase_solana = float(coinbase_solana())
        bot.send_message(message.from_user.id, f'1 DOGE = {coinbase_doge} USD \n1 BTC = {coinbase_btc} USD \n1 ETC = {coinbase_etc} USD \n1 DASH = {coinbase_dash} USD \n1 REP = {coinbase_augur} USD \n1 SOL = {coinbase_solana} USD');
        bot.send_message(message.from_user.id, 'If you want to know more, type /start');
    elif exchange == 'Kraken':
        bot.send_message(message.from_user.id, 'Wait please...')
        kraken_btc = float(kraken_btc())
        kraken_doge = float(kraken_doge())
        kraken_etc = float(kraken_etc())
        kraken_dash = float(kraken_dash())
        kraken_augur = float(kraken_augur())
        kraken_solana = float(kraken_solana())
        bot.send_message(message.from_user.id, f'1 DOGE = {kraken_doge} USDT \n1 BTC = {kraken_btc} USDT \n1 ETC = {kraken_etc} USD \n1 DASH = {kraken_dash} USD \n1 REP = {kraken_augur} USD \n1 SOL = {kraken_solana} USDT');
        bot.send_message(message.from_user.id, 'If you want to know more, type /start');
    elif exchange == 'KuCoin':
        bot.send_message(message.from_user.id, 'Wait please...')
        kucoin_btc = float(kucoin_btc())
        kucoin_doge = float(kucoin_doge())
        kucoin_etc = float(kucoin_etc())
        kucoin_dash = float(kucoin_dash())
        kucoin_augur = float(kucoin_augur())
        kucoin_solana = float(kucoin_solana())
        bot.send_message(message.from_user.id, f'1 DOGE = {kucoin_doge} USDT \n1 BTC = {kucoin_btc} USDT \n1 ETC = {kucoin_etc} USDT \n1 DASH = {kucoin_dash} USDT \n1 REP = {kucoin_augur} USDT \n1 SOL = {kucoin_solana} USDT');
        bot.send_message(message.from_user.id, 'If you want to know more, type /start');
    else:
        bot.send_message(message.from_user.id, 'Choose exchange from menu please!');
        bot.register_next_step_handler(message, exchange);



def crypto1(message): #получаем фамилию
    currency = message.text;
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

    if currency == 'DogeCoin':
        bot.send_message(message.from_user.id,'Wait please...')
        binance_doge = float(binance_doge())
        coinbase_doge = float(coinbase_doge())
        kraken_doge = float(kraken_doge())
        kucoin_doge = float(kucoin_doge())
        bot.send_message(message.from_user.id, f'1 DOGE = {binance_doge} USDT(Binance) \n1 DOGE = {coinbase_doge} USD(Coinbase) \n1 DOGE = {kraken_doge} USDT(Kraken) \n1 DOGE = {kucoin_doge} USDT(KuCoin)');
        bot.send_message(message.from_user.id, 'If you want to know more, type /start');
    elif currency == 'Bitcoin':
        bot.send_message(message.from_user.id,'Wait please...')
        binance_btc = float(binance_btc())
        coinbase_btc = float(coinbase_btc())
        kraken_btc = float(kraken_btc())
        kucoin_btc = float(kucoin_btc())
        bot.send_message(message.from_user.id, f'1 BTC = {binance_btc} USDT(Binance) \n1 BTC = {coinbase_btc} USD(Coinbase) \n1 BTC = {kraken_btc} USDT(Kraken) \n1 BTC = {kucoin_btc} USDT(KuCoin)');
        bot.send_message(message.from_user.id, 'If you want to know more, type /start');
    elif currency == 'Etherium':
        bot.send_message(message.from_user.id,'Wait please...')
        binance_etc = float(binance_etc())
        coinbase_etc = float(coinbase_etc())
        kraken_etc = float(kraken_etc())
        kucoin_etc = float(kucoin_etc())
        bot.send_message(message.from_user.id, f'1 ETC = {binance_etc} USDT(Binance) \n1 ETC = {coinbase_etc} USD(Coinbase) \n1 ETC = {kraken_etc} USD(Kraken) \n1 ETC = {kucoin_etc} USDT(KuCoin)');
        bot.send_message(message.from_user.id, 'If you want to know more, type /start');
    elif currency == 'DASH':
        bot.send_message(message.from_user.id,'Wait please...')
        binance_dash = float(binance_dash())
        coinbase_dash = float(coinbase_dash())
        kraken_dash = float(kraken_dash())
        kucoin_dash = float(kucoin_dash())
        bot.send_message(message.from_user.id, f'1 DASH = {binance_dash} USDT(Binance) \n1 DASH = {coinbase_dash} USD(Coinbase) \n1 DASH = {kraken_dash} USD(Kraken) \n1 DASH = {kucoin_dash} USDT(KuCoin)');
        bot.send_message(message.from_user.id, 'If you want to know more, type /start');
    elif currency == 'Augur':
        bot.send_message(message.from_user.id,'Wait please...')
        binance_augur = float(binance_augur())
        coinbase_augur = float(coinbase_augur())
        kraken_augur = float(kraken_augur())
        kucoin_augur = float(kucoin_augur())
        bot.send_message(message.from_user.id, f'1 REP = {binance_augur} USDT(Binance) \n1 REP = {coinbase_augur} USD(Coinbase) \n1 REP = {kraken_augur} USD(Kraken) \n1 REP = {kucoin_augur} USDT(KuCoin)');
        bot.send_message(message.from_user.id, 'If you want to know more, type /start');
    elif currency == 'Solana':
        bot.send_message(message.from_user.id,'Wait please...')
        binance_solana = float(binance_solana())
        coinbase_solana = float(coinbase_solana())
        kraken_solana = float(kraken_solana())
        kucoin_solana = float(kucoin_solana())
        bot.send_message(message.from_user.id, f'1 SOL = {binance_solana} USDT(Binance) \n1 SOL = {coinbase_solana} USD(Coinbase) \n1 SOL = {kraken_solana} USDT(Kraken) \n1 SOL = {kucoin_solana} USDT(KuCoin)');
        bot.send_message(message.from_user.id, 'If you want to know more, type /start');
    else:
        bot.send_message(message.from_user.id, 'Choose currency from menu please!');
        bot.register_next_step_handler(message, crypto1);

bot.polling(none_stop=True)
