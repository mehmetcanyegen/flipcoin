'''
Created on Jan 9, 2018

@author: mehmetcan
'''

import Bittrex 
import Poloniex
import Kucoin
import Bitz
import json
import requests
import Data

def getFromBittrex():
    response = requests.get(Bittrex.url)
    js = json.loads(response.content)
    for i in js['result']:
        if(i['MarketName'].split("-")[0] == "BTC"):
            tag = i['MarketName'].split("-")[1]
            buy =  i['Bid']
            sell =  i['Ask']
            Data.reloadCoinValue(tag, 'bittrex', sell, buy)

def getFromPoloniex():
    response = requests.get(Poloniex.url)
    js = json.loads(response.content)
    for i in js:
        if(i.split("_")[0] == "BTC"):
            tag = i.split("_")[1]
            buy = js[i]['highestBid']
            sell = js[i]['lowestAsk']
            Data.reloadCoinValue(tag, 'poloniex', sell, buy) 

def getFromKucoin():
    response = requests.get(Kucoin.url)
    js = json.loads(response.content)
    for i in js['data']:
        if(i['symbol'].split("-")[1] == "BTC"):
            tag = i['symbol'].split("-")[0]
            sell = i['sell']
            buy = i['buy']
            Data.reloadCoinValue(tag, 'kucoin', sell, buy)

def getFromBitz():
    response = requests.get(Bitz.url)
    js = json.loads(response.content)
    for i in js['data']:
        if(i.split("_")[1] == "btc"):
            tag = i.split("_")[0].upper()
            sell = js['data'][i]['sell']
            buy = js['data'][i]['buy']
            Data.reloadCoinValue(tag, 'bitz', sell, buy)


            
            