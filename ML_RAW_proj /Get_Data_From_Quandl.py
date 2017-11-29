import quandl
import os
import pandas as pd
import time



quandl.ApiConfig.api_key ='p4QD1b3jojZabYXs45u9'
#data = quandl.get_table('WIKI/PRICES',
#                        qopts = { 'columns': ['ticker', 'date', 'adj_close'] },
#                        ticker = ['AAPL', 'MSFT'],
#                        date = { 'gte': '2016-01-01', 'lte': '2016-12-31' })
#
#data_df = pd.DataFrame()
#data_df = data
#data_df.to_csv('Quandl_Data.csv')


path = '/Users/Wen/Desktop/intraQuarter'

def Get_Price_From_Quandl():
    df = pd.DataFrame()
    statspath = path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    first_row = 1


    for each_dir in stock_list[1:]:
        ticker = each_dir.split('KeyStats/')[1]
        name = ticker.upper()
        data = quandl.get_table('WIKI/PRICES',
                                qopts={'columns':['date','adj_close']},
                                ticker=name,
                                date={'gte':'2000-01-01',
                                      'lte':'2014-12-30'})
        data[name] = data['adj_close']
        if first_row == 1:
            df=pd.concat([df,data['date']],axis=1)
            first_row+=1
        
        df=pd.concat([df,data[name]],axis = 1)
        df.to_csv('QuandlPrice.csv')
    






Get_Price_From_Quandl()
    



