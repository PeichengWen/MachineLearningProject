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
    data_df = pd.read_csv("KeyData.csv")

    X = np.array(data_df[features].values)
    y = np.array(data_df["Status"].replace("outperform",1).replace("underperform",0).values)

    
    
    X = preprocessing.scale(X)

    
    return X,y



def Train_Test():

    test_size = 1000
    

    X,y = Get_Data()
    clf = svm.SVC(kernel="linear",C=1.0)
    clf.fit(X[:-test_size],y[:-test_size])

    correct_count = 0

    try:

        for x in range(1,test_size+1):
            if clf.predict(X[-x].reshape(1,-1))[0] == y[-x]:
                correct_count+=1
    except Exception as e:
        print(e)
            
    print("Acuracy:",(correct_count/test_size)*100.00)



Train_Test()










    
