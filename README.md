# flipcoin

flipcoin is a python wrapper library to connect different crypto coin markets

# usage

```
import flipcoin

flipcoin.getFromBittrex()
flipcoin.getFromPoloniex()
flipcoin.getFromKucoin()
flipcoin.getFromBitz()

print(flipcoin.Data.AllCoins['DGB']['bittrex']['buy'])

```
