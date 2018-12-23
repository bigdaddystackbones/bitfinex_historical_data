##################################################################################
######################### START GENERAL AREA #####################################
##################################################################################

import sys
import time
from datetime import datetime
import requests
import datetime as dt
import pandas as pd
import json
import csv
import numpy as np
from numpy import genfromtxt

# -----------------------------------------------------------------------------

def get_bitfinex_data(coin, time_intervall, fill_empty_rows):
    url = 'https://api.bitfinex.com/v2/candles/trade:'+time_intervall+':t'+coin+'/hist'

    #define time intervall to get data from bitfinex (bitfinex querys have a limit)
    #28.800.000 = 480 rows for minute and = 96 rows for 5m

    if time_intervall == '1m': 
        time_intervall_ms_query = 48000000.0
        time_intervall_ms_query_2 = 60000
        time_intervall2 = '1Min'
    if time_intervall == '5m':
        time_intervall_ms_query = 240000000.0
        time_intervall_ms_query_2 = 300000
        time_intervall2 = '5Min'
    if time_intervall == '15m':
        time_intervall_ms_query = 720000000.0
        time_intervall_ms_query_2 = 4500000
        time_intervall2 = '15Min'
    if time_intervall == '30m':
        time_intervall_ms_query = (720000000.0 * 2)
        time_intervall_ms_query_2 = (4500000 * 2)
        time_intervall2 = '30Min'
    if time_intervall == '1H':
        time_intervall_ms_query = (720000000.0 * 4)
        time_intervall_ms_query_2 = (4500000 * 4)
        time_intervall2 = '1H'
    if time_intervall == '4H':
        time_intervall_ms_query = (720000000.0 * 16)
        time_intervall_ms_query_2 = (4500000 * 16)
        time_intervall2 = '4H'
    if time_intervall == '6H':
        time_intervall_ms_query = (720000000.0 * 24)
        time_intervall_ms_query_2 = (4500000 * 24)
        time_intervall2 = '6H'
    if time_intervall == '12H':
        time_intervall_ms_query = (720000000.0 * 48)
        time_intervall_ms_query_2 = (4500000 * 48)
        time_intervall2 = '12H'
    if time_intervall == 'D':
        time_intervall_ms_query = (720000000.0 * 96)
        time_intervall_ms_query_2 = (4500000 * 96)
        time_intervall2 = 'D'
    if time_intervall == 'W':
        time_intervall_ms_query = (720000000.0 * 336)
        time_intervall_ms_query_2 = (4500000 * 336)
        time_intervall2 = 'W'

    # -------------------

    #Set intervals
    test1_date = start_date
    test2_date = start_date + time_intervall_ms_query

    # -------------------

    pricedata = pd.DataFrame()

    #Get data with time intervals
    while test1_date < curr_date:
        print(test2_date, 'Fetching candles starting from', test1_date)
        params = { 'start': test1_date, 'end': test2_date, 'sort': 1 }
        
        r = requests.get(url, params = params)

        test1_date = test2_date + time_intervall_ms_query
        test2_date = test2_date + time_intervall_ms_query + time_intervall_ms_query_2

        data = r.json()
        
        for i in data:  
            i[0] = (i[0]/1000)

        data = pd.DataFrame(data)

        pricedata = pd.concat([pricedata, data])
        time.sleep(3)

    # -------------------
    #fill empty rows with values form timestamp before
    if fill_empty_rows == True:
        pricedata = pricedata.set_index([0])
        pricedata = pricedata.drop(pricedata.index[0])
        pricedata.index = pd.to_datetime(pricedata.index, unit='s')
        pricedata = pricedata.asfreq(freq = time_intervall2, method='pad')
    
    # -------------------
    #write data to csv
    pricedata.to_csv('pricedata'+str(coin)+'_'+str(time_intervall)+'.csv', sep=',')


##################################################################################
######################### START INDIVIDUAL AREA ##################################
##################################################################################

#define start date
start = '01.12.2018 09:00:00,00'
# -----------------------------------------------------------------------------

#transform date to milliseconds
start_date = datetime.strptime(start,
                           '%d.%m.%Y %H:%M:%S,%f')

start_date = start_date.timestamp() * 1000
curr_date = round(time.time(),4) * 1000.0

print('Start date: {0}'.format(start))
print('Current date: {0}'.format(curr_date))

# -----------------------------------------------------------------------------

get_coins = ['ZRXBTC', 'QTMBTC', 'ZECBTC', 'ETCBTC', 'XMRBTC', 'ETHBTC', 'NEOBTC',
            'LTCBTC', 'IOTBTC', 'XRPBTC', 'XLMBTC', 'ETPBTC', 'TRXBTC', 'BATBTC',
            'VETBTC', 'IOSBTC', 'POYBTC', 'QSHBTC', 'DATBTC', 'OMGBTC', 'ELFBTC']

#possible time intervalls: 1m/5m/15m/30m/1H/4H/6H/12H/D/W
time_intervall = '5m'

##################################################################################
########################### END INDIVIDUAL AREA ##################################
##################################################################################

#call function get_bitfinex_data 
for i in get_coins:
    get_bitfinex_data(i, time_intervall, fill_empty_rows=True)
