import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm,preprocessing
from sklearn.preprocessing import  Imputer  
import pandas as pd
from matplotlib import style
import time

style.use("ggplot")


features = ['DE Ratio',
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
features_selected = ['Forward P/E',
                    'Diluted EPS',
                    'DE Ratio',
                    'Trailing P/E',
                    'Price/Sales',
                    'Price/Book',
                    'Profit Margin',
                    'Operating Margin',
                    'Return on Assets',
                    'Revenue Per Share',
                    'Market Cap',
                    'Enterprise Value',
                    'Enterprise Value/Revenue',
                    'Enterprise Value/EBITDA',
                    'Revenue',
                    'Gross Profit',
                    'Net Income Avl to Common ',
                    'Earnings Growth',
                    'Revenue Growth',
                    'Total Cash',
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
                    'Shares Short (prior '  ]



def Get_Data():
    data_df = pd.read_csv("Full_NewKeyData_quandl.csv")
    data_df = data_df.fillna('N/A')
    data_df = data_df.replace('N/A',np.nan)
    
    data_df = data_df.reindex(np.random.permutation(data_df.index))
    
    X = np.array(data_df[features].values)
    imp=Imputer(missing_values='NaN',strategy='mean',axis=0)
    imp.fit(X)
    X = imp.transform(X)
    y = np.array(data_df["Status"].replace("outperform",1).replace("underperform",0).values)
       
    X_mean = X.mean(axis=0)
    X_std = X.std(axis=0)
    X = (X-X_mean)/X_std

    
    return X,y



def Train_Test():
    
        test_size = 500
        test_times = 100
        accuracy_sum = 0
        
        for i in range(test_times):
            X,y = Get_Data()
            clf = svm.SVC(kernel="rbf",
                          C=14,
                          gamma=1)
            clf.fit(X[:-test_size],y[:-test_size])
            correct_count = 0
            
            for x in range(1,test_size+1):
                if clf.predict(X[-x].reshape(1,-1)) == y[-x]:
                    correct_count+=1
                    
            accuracy_sum += (correct_count/test_size)*100.00

        print(len(y))
        print("Acuracy:",round((accuracy_sum/test_times),2))

        
Train_Test()










    
