'''
Created on Jan 9, 2018

@author: mehmetcan
'''
 
AllCoins = {}


def reloadCoinValue(tag, market, sell, buy ):

    if tag not in AllCoins:
        AllCoins[tag] = {}
        
    if market not in AllCoins[tag]:
        AllCoins[tag][market] = {}
        
    AllCoins[tag][market]['sell'] = sell
    AllCoins[tag][market]['buy'] = buy
 
    