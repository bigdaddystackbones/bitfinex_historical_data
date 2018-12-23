# cryptocurrency_data
Hi all,

I like to provide python code for getting bifinex pricing data.
Bitfinex querys have a limit so you can't get pricing data for a longer time and need to run multiple queries.


Basics:
You need to download to following packages  to run the code:
- datetime
- numpy
- requests
- pandas

The code is split into a general area and a individual area.
The general area defines the functions necessary to download the pricing data.
In the indiviual area you can set the time horizon for which you like to get data. You can also define the coins in which you are interested.

The data is about 1m/5m/15m/30m/1H/4H/6H/12H/D/W candlestick data
You can set the time frequency in the individual area.

After running the code the data is stored as a csv data in your workspace. 
Each row contains:  timestamp, open, close, high, low, volume

Note: 
If the coin you like to get data about a coin that is rather small, has low traing volume and your time frequency is low, it can be the case that bitfinex gives you no data for some points in time. My code fills this points with the price from the last point in time were data is avaiable. Consider follwing example:

- t-2: price is 1
- t-1: price is 2
- t: bitfinex doesn't give you data for t because the price hasn't changed --> price is still 2


I appreciate every feedback regarding the code.
You can send an email to bigdaddystackbones@protonmail.com



#---------------------------
Donations and ref links:

- BTC address: 1YPGau94txFpXc3KR658u9exrk1X8ycd1
- bitmex ref-link: https://www.bitmex.com/register/mXgr8t
- binance ref-link: https://www.binance.com/?ref=35066436


