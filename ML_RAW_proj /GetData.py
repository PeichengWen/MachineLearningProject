import os
import time
import pandas as pd
from datetime import datetime

from time import mktime
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
style.use("dark_background")

import re



path="/Users/WEN/Desktop/intraQuarter"

def Key_Stats(gather=["Total Debt/Equity",
                      'Trailing P/E',
                      'Price/Sales',
                      'Price/Book',
                      'Profit Margin',
                      'Operating Margin',
                      'Return on Assets',
                      'Return on Equity',
                      'Revenue Per Share',
                      'Market Cap',
                      'Enterprise Value',
                      'Forward P/E',
                      'PEG Ratio',
                      'Enterprise Value/Revenue',
                      'Enterprise Value/EBITDA',
                      'Revenue',
                      'Gross Profit',
                      'EBITDA',
                      'Net Income Avl to Common ',
                      'Diluted EPS',
                      'Earnings Growth',
                      'Revenue Growth',
                      'Total Cash',
                      'Total Cash Per Share',
                      'Total Debt',
                      'Current Ratio',
                      'Book Value Per Share',
                      'Cash Flow',
                      'Beta',
                      'Held by Insiders',
                      'Held by Institutions',
                      'Shares Short (as of',
                      'Short Ratio',
                      'Short % of Float',
                      'Shares Short (prior ']):
  statspath = path+'/_KeyStats'
  stock_list = [x[0] for x in os.walk(statspath)]
  #print (stock_list)
  df = pd.DataFrame(columns = ['Date',
                               'Unix',
                               'Ticker',
                               'Price',
                               'price_p_change',
                               'sp500',
                               'sp500_p_change',
                               'Difference',                              
                               'DE Ratio',
                               'Trailing P/E',
                               'Price/Sales',
                               'Price/Book',
                               'Profit Margin',
                               'Operating Margin',
                               'Return on Assets',
                               'Return on Equity',
                               'Revenue Per Share',
                               'Market Cap',
                               'Enterprise Value',
                               'Forward P/E',
                               'PEG Ratio',
                               'Enterprise Value/Revenue',
                               'Enterprise Value/EBITDA',
                               'Revenue',
                               'Gross Profit',
                               'EBITDA',
                               'Net Income Avl to Common ',
                               'Diluted EPS',
                               'Earnings Growth',
                               'Revenue Growth',
                               'Total Cash',
                               'Total Cash Per Share',
                               'Total Debt',
                               'Current Ratio',
                               'Book Value Per Share',
                               'Cash Flow',
                               'Beta',
                               'Held by Insiders',
                               'Held by Institutions',
                               'Shares Short (as of',
                               'Short Ratio',
                               'Short % of Float',
                               'Shares Short (prior ', 
                               'Status'])
  sp500_df = pd.read_csv("SP500History.csv",index_col='Date')
  price_df = pd.read_csv("QuandlPrice.csv",index_col='date')
  

  ticker_list = []
  

  for each_dir in stock_list[1:]:
    each_file = os.listdir(each_dir)
    ticker = each_dir.split('Stats/')[1]

    ticker_list.append(ticker)

    starting_price_value = False
    starting_sp500_value = False
    if len(each_file) > 0:
        for file in each_file:
            date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
            unix_time = time.mktime(date_stamp.timetuple())
            full_file_path = each_dir+'/'+file
            source = open(full_file_path,'r',encoding="utf-8").read()
            try:
              value_list = []


              
              for each_name in gather:
                
                try:
                  nor_name = re.escape(each_name) + r'.*?(\d{1,8}.\d{1,8}M?B?|N/A)%?</td>'
                  search_value = re.search(nor_name,source)
                  value = (search_value.group(1))
                  if "B" in value:
                    value = float(value.replace("B",""))*1000000000
                  elif "M" in value:
                    value = float(value.replace("M",""))*1000000
                    


                  value_list.append(value)
                  #print(value)
                  
                except:
                  value = "N/A"
                  value_list.append(value)

              one_year=int(unix_time+31104000)

              try:
                sp500_date=datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d')
                row = sp500_df[(sp500_df.index == sp500_date)]
                sp500_value = float(row['SP500'])
              except:
                sp500_date=datetime.fromtimestamp(unix_time-259200).strftime('%Y-%m-%d')
                row = sp500_df[(sp500_df.index == sp500_date)]
                sp500_value = float(row['SP500'])
              try:
                sp500_date_1y=datetime.fromtimestamp(one_year).strftime('%Y-%m-%d')
                row = sp500_df[(sp500_df.index == sp500_date_1y)]
                sp500_value_1y = float(row['SP500'])
              except:
                sp500_date_1y=datetime.fromtimestamp(one_year-259200).strftime('%Y-%m-%d')
                row = sp500_df[(sp500_df.index == sp500_date_1y)]
                sp500_value_1y = float(row['SP500'])



              try:
                price_date=datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d')
                row = price_df[(price_df.index == price_date)]
                stock_price = float(row[ticker.upper()])
              except:
                price_date=datetime.fromtimestamp(unix_time-259200).strftime('%Y-%m-%d')
                row = price_df[(price_df.index == price_date)]
                stock_price = float(row[ticker.upper()])


              try:
                price_date_1y=datetime.fromtimestamp(one_year).strftime('%Y-%m-%d')
                row = price_df[(price_df.index == price_date_1y)]
                stock_price_1y = float(row[ticker.upper()])
              except:
                sp500_date_1y=datetime.fromtimestamp(one_year-259200).strftime('%Y-%m-%d')
                row = sp500_df[(sp500_df.index == sp500_date_1y)]
                sp500_value_1y = float(row[ticker.upper()])


              
                
              


              
                


              price_p_change = (stock_price_1y - stock_price) / stock_price *100
              sp500_p_change = (sp500_value_1y - sp500_value) / sp500_value *100
              #starting_price_value = stock_price
              #starting_sp500_value = sp500_value

              difference = price_p_change-sp500_p_change

              if difference > 0:
                status = "outperform"
              else:
                status = "underperform"


              if value_list.count("N/A")>15:
                pass
              else:
                #print(value_list[0])
                #time.sleep(10)
                try:
                  df = df.append({'Date':date_stamp,
                                  'Unix':unix_time,
                                  'Ticker':ticker,
                                  'Price':stock_price,
                                  'price_p_change':price_p_change,
                                  'sp500':sp500_value,
                                  'sp500_p_change':sp500_p_change,
                                  'Difference':difference,
                                  'DE Ratio':value_list[0],
                                  'Trailing P/E':value_list[1],
                                  'Price/Sales':value_list[2],
                                  'Price/Book':value_list[3],
                                  'Profit Margin':value_list[4],
                                  'Operating Margin':value_list[5],
                                  'Return on Assets':value_list[6],
                                  'Return on Equity':value_list[7],
                                  'Revenue Per Share':value_list[8],
                                  'Market Cap':value_list[9],
                                  'Enterprise Value':value_list[10],
                                  'Forward P/E':value_list[11],
                                  'PEG Ratio':value_list[12],
                                  'Enterprise Value/Revenue':value_list[13],
                                  'Enterprise Value/EBITDA':value_list[14],
                                  'Revenue':value_list[15],
                                  'Gross Profit':value_list[16],
                                  'EBITDA':value_list[17],
                                  'Net Income Avl to Common ':value_list[18],
                                  'Diluted EPS':value_list[19],
                                  'Earnings Growth':value_list[20],
                                  'Revenue Growth':value_list[21],
                                  'Total Cash':value_list[22],
                                  'Total Cash Per Share':value_list[23],
                                  'Total Debt':value_list[24],
                                  'Current Ratio':value_list[25],
                                  'Book Value Per Share':value_list[26],
                                  'Cash Flow':value_list[27],
                                  'Beta':value_list[28],
                                  'Held by Insiders':value_list[29],
                                  'Held by Institutions':value_list[30],
                                  'Shares Short (as of':value_list[31],
                                  'Short Ratio':value_list[32],
                                  'Short % of Float':value_list[33],
                                  'Shares Short (prior ':value_list[34],
                                  'Status':status},ignore_index = True)
                except Exception as e:
                  print (e)
            except Exception as e:
              pass



  
 # save = gather.replace(' ','').replace('(','').replace(')','').replace('/','')+'.csv'
  print('save')
  df.to_csv("Full_NewKeyData_quandl.csv")
            
  
            




Key_Stats()

  
  
