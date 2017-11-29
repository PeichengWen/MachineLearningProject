import os
import time
import pandas as pd
from datetime import datetime



path="/Users/WEN/Desktop/intraQuarter"

def Key_Stats(gather="Total Debt/Equity (mrq)"):
  statspath = path+'/_KeyStats'
  stock_list = [x[0] for x in os.walk(statspath)]
  #print (stock_list)
  df = pd.DataFrame(columns = ['Date',
                               'Unix',
                               'Ticker',
                               'DE Ratio',
                               'Price',
                               'price_p_change',
                               'sp500',
                               'sp500_p_change'])
  sp500_df = pd.read_csv("SP500History.csv",index_col='Date')

  for each_dir in stock_list[1:25]:
    each_file = os.listdir(each_dir)
    ticker = each_dir.split('Stats/')[1]

    starting_price_value = False
    starting_sp500_value = False
    if len(each_file) > 0:
        for file in each_file:
            date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
            unix_time = time.mktime(date_stamp.timetuple())
            full_file_path = each_dir+'/'+file
            source = open(full_file_path,'r',encoding="utf-8").read()
            try:
              value = float(source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])
              try:
                sp500_date=datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d')
                row = sp500_df[(sp500_df.index == sp500_date)]
                sp500_value = float(row['SP500'])
              except:
                sp500_date=datetime.fromtimestamp(unix_time-259200).strftime('%Y-%m-%d')
                row = sp500_df[(sp500_df.index == sp500_date)]
                sp500_value = float(row['SP500'])
                
              

              stock_price = float(source.split('</small><big><b>')[1].split('</b></big>')[0])
              if not starting_price_value:
                starting_price_value = stock_price
              if not starting_sp500_value:
                starting_sp500_value = sp500_value


              price_p_change = (stock_price - starting_price_value) / starting_price_value *100
              sp500_p_change = (sp500_value - starting_sp500_value) / starting_sp500_value *100
              starting_price_value = stock_price
              starting_sp500_value = sp500_value



              
              df = df.append({'Date':date_stamp,
                              'Unix':unix_time,
                              'Ticker':ticker,
                              'DE Ratio':value,
                              'Price':stock_price,
                              'price_p_change':price_p_change,
                              'sp500':sp500_value,
                              'sp500_p_change':sp500_p_change},ignore_index = True)
            except Exception as e:
              pass

  save = gather.replace(' ','').replace('(','').replace(')','').replace('/','')+'.csv'
  print(save)
  df.to_csv(save)
            
  
            




Key_Stats()

  
  
