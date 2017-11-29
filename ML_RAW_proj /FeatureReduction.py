import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm,preprocessing
import pandas as pd
from matplotlib import style
import time

style.use("ggplot")


features = ['Forward P/E',
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
    data_df = pd.read_csv("KeyData.csv")

    data_df = data_df.reindex(np.random.permutation(data_df.index))

    X = np.array(data_df[features].values)
    y = np.array(data_df["Status"].replace("outperform",1).replace("underperform",0).values)

    
    
    #X = preprocessing.scale(X)
    X_mean = X.mean(axis=0)
    X_std = X.std(axis=0)
    X = (X-X_mean)/X_std

    
    return X,y



def Train_Test():
    #for feature in features:
    
        test_size = 500
        test_times = 100
        accuracy_sum = 0
        
        for i in range(test_times):
            X,y = Get_Data()
            clf = svm.SVC(kernel="linear",C=1.0)
            clf.fit(X[:-test_size],y[:-test_size])

            correct_count = 0
            for x in range(1,test_size+1):
               if clf.predict(X[-x].reshape(1,-1)) == y[-x]:
                    correct_count+=1
                    
            accuracy = (correct_count/test_size)*100.00
            accuracy_sum +=accuracy

        accuracy = accuracy_sum/test_times

        

        
        
                
        print("Accuracy:",accuracy)



    



Train_Test()










    
