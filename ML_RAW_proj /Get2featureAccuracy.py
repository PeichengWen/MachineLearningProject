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
feature = ['DE Ratio','Trailing P/E']


def Get_Data(feature):
    data_df = pd.read_csv("KeyData.csv")

    data_df = data_df.reindex(np.random.permutation(data_df.index))

    X = np.array(data_df[feature].values)
    y = np.array(data_df["Status"].replace("outperform",1).replace("underperform",0).values)

    
    
    #X = preprocessing.scale(X)
    X_mean = X.mean(axis=0)
    X_std = X.std(axis=0)
    X = (X-X_mean)/X_std

    
    return X,y



def Train_Test():
    accuracy_df = pd.DataFrame(columns = ["Feature1","Feature2","accuracy"])
    features_num = len(features)
    
    for i in range(0,features_num):
        
        for j in range(i,features_num):

            feature = [features[i],features[j]]
          
            test_size = 1000
            accuracy_sum = 0
            test_times = 10
            
            for m in range(test_times):
                X,y = Get_Data(feature)
                clf = svm.SVC(kernel="linear",C=1.0)
                clf.fit(X[:-test_size],y[:-test_size])

                correct_count = 0

                for x in range(1,test_size+1):
                    if clf.predict(X[-x].reshape(1,-1)) == y[-x]:
                            correct_count+=1
                accuracy = (correct_count/test_size)*100.00
                #print(accuracy)
                accuracy_sum +=accuracy

            accuracy = accuracy_sum/test_times
            #print('average:',accuracy)

            
            accuracy_df = accuracy_df.append({"Feature1":features[i],"Feature2":features[j],"accuracy":accuracy},ignore_index=True)
    accuracy_df.to_csv("2featuresAccuracy.csv")
                        
            
                
    #print(features[i],' ',features[j],':')
    #print("Accuracy:",accuracy)



    



Train_Test()













    
