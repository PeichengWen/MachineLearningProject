import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm,preprocessing
import pandas as pd
from matplotlib import style
import time

style.use("ggplot")


features = [                   'DE Ratio',
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
                               'Shares Short (prior ']



def Get_Data():
    data_df = pd.read_csv("NewKeyData_quandl.csv")
    data_df = data_df.replace('N/A',0)
    data_df = data_df.fillna(0)

    data_df = data_df.reindex(np.random.permutation(data_df.index))
    

    X = np.array(data_df[features].values)
    y = np.array(data_df["Status"].replace("outperform",1).replace("underperform",0).values)
    Z = np.array(data_df[['price_p_change','sp500_p_change']])

    
    
    #X = preprocessing.scale(X)
    X_mean = X.mean(axis=0)
    X_std = X.std(axis=0)
    X = (X-X_mean)/X_std

    
    return X,y,Z



def Train_Test():
    #for feature in features:
    
        test_size = 500
        test_times = 100
        accuracy_sum = 0
        market_return = 0
        invest_return = 0
        total_market_return = 0
        total_invest_return = 0
        invest_amount = 1000
        number_of_invest=0
        total_invest_money = 0

        
        
        for i in range(test_times):
            X,y,Z = Get_Data()
            
            clf = svm.SVC(kernel="rbf",C=1.0)
            clf.fit(X[:-test_size],y[:-test_size])

            correct_count = 0

            for x in range(1,test_size+1):
                if clf.predict(X[-x].reshape(1,-1)) == y[-x]:
                    correct_count+=1
                if clf.predict(X[-x].reshape(1,-1)) == 1:
                    market_return = invest_amount*(1+Z[-x][1]/100)
                    invest_return = invest_amount*(1+Z[-x][0]/100)
                    
                    number_of_invest +=1
                    total_market_return +=market_return
                    total_invest_return +=invest_return
                    
                    
                    
                
            accuracy = (correct_count/test_size)*100.00
            accuracy_sum += accuracy

        accuracy = round((accuracy_sum/test_times),2)
        total_market_return = total_market_return/test_times
        total_invest_return = total_invest_return/test_times
        number_of_invest = round(number_of_invest/test_times,0)
        total_invest_money=invest_amount*number_of_invest
       

        cp_to_market=round(((total_invest_return-total_market_return)/total_market_return)*100,2)
        cp_to_original=round(((total_invest_return-total_invest_money)/total_invest_money)*100,2)
        
        
                        
        
        print("Acuracy:",accuracy)
        print("If our total amount money for investing is: ",total_invest_money)
        print("We can earn: ",cp_to_original,"% more.")
        print("Compare to the market, we can earn: ",cp_to_market,"% more.")
        

    



Train_Test()










    
