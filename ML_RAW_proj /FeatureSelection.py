import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm,preprocessing
import pandas as pd
from matplotlib import style
import time

style.use("ggplot")


features = [                   'Forward P/E',
                               'Diluted EPS',
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
                               
                               'PEG Ratio',
                               'Enterprise Value/Revenue',
                               'Enterprise Value/EBITDA',
                               'Revenue',
                               'Gross Profit',
                               'EBITDA',
                               'Net Income Avl to Common ',
                               
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









def Draw_figures():
    
    features_num = len(features)
    data_df = pd.read_csv("KeyData.csv")
    x=data_df[features[1]]
    x_mean = x.mean(axis=0)
    x_std = x.std(axis=0)
    x = (x-x_mean)/x_std

    for i in range(2,features_num):
        plt.figure()
 
        
        y=data_df[features[i]]
        y_mean = y.mean(axis=0)
        y_std = y.std(axis=0)
        y = (y-y_mean)/y_std
        plt.xlabel(features[0])
        plt.ylabel(features[i])
        plt.plot(x,y,'ro',label='point')
    plt.show()




Draw_figures()
    
    
    

 












    
