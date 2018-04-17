# This bot will retrieve price data and post it on the Steem Blockchain.

from steem import Steem
import urllib.request
import json
import random

gifs = ["https://media.giphy.com/media/pVVsPksfZrgiXrjjvt/giphy.gif", "https://media.giphy.com/media/3osBLlcDmJBOQbSGMU/giphy.gif", "https://media.giphy.com/media/3HFiX05GITTe1SAh9F/giphy.gif", "https://media.giphy.com/media/3o7WIKAFr8OweEbABi/giphy.gif", "https://media.giphy.com/media/xULW8MIrFV8pyZjChi/giphy.gif", "https://media.giphy.com/media/kPLWwi6cXZwMo/giphy.gif", "https://media.giphy.com/media/7FBY7h5Psqd20/giphy.gif", "https://media.giphy.com/media/cnw1DaX3giYGk/giphy.gif"]
gif = random.choice(gifs)

url = urllib.request.urlopen('https://poloniex.com/public?command=returnTicker')
result = url.read()
resultj = json.loads(result)

BTC = resultj['USDT_BTC']['last']
BTC = float(BTC)
BTC = round(BTC, 2)
STEEM = resultj['BTC_STEEM']['last']
STEEM = float(STEEM) * float(BTC)
STEEM = round(STEEM, 2)
SBD = resultj['BTC_SBD']['last']
SBD = float(SBD) * float(BTC)
SBD = round(SBD, 2)

print ("posting prices...")
s = Steem(keys=["YOUR POSTING KEY"])
s.commit.post(
    "Todays Daily Market: STEEM @ {} ...".format(STEEM),
    "**Bitcoin:** {} USD".format(BTC) + "<br>**Steem:** {}".format(STEEM) + "<br>**Steem Dollars:** {}<br>".format(SBD) + "<br>*This is an automated msg posted by the [price_bot.py](https://github.com/PixelNoob/python-steem)* <br>" + gif,
    "YOUR ACCOUNT",
    tags=["bitcoin","steem", "trade"]
)

print ("prices posted succesfully")
