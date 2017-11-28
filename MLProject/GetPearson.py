import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm,preprocessing
import pandas as pd
from matplotlib import style
import time
from scipy.stats import pearsonr
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
feature1 = ['DE Ratio']
feature2 = ['Trailing P/E']


def Get_Data(feature1,feature2):
    data_df = pd.read_csv("Full_NewKeyData_quandl.csv")
    data_df = data_df.replace('N/A',0)
    data_df = data_df.fillna(0)

    

    data_df = data_df.reindex(np.random.permutation(data_df.index))

    X1 = np.array(data_df[feature1].values)
    X2 = np.array(data_df[feature2].values)
    y = np.array(data_df["Status"].replace("outperform",1).replace("underperform",0).values)

    
    
    #X = preprocessing.scale(X)
    X1_mean = X1.mean(axis=0)
    X1_std = X1.std(axis=0)
    X1 = (X1-X1_mean)/X1_std
    X2_mean = X2.mean(axis=0)
    X2_std = X2.std(axis=0)
    X2 = (X2-X2_mean)/X2_std

    
    return X1,X2,y



def Train_Test():
    accuracy_df = pd.DataFrame(columns = ['Feature',
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
                               'Shares Short (prior '])
    features_num = len(features)
    
    for i in range(0,features_num):
        pearson = []
        
        for j in range(0,features_num):

            feature1 = features[i]
            feature2 = features[j]
            X1,X2,y = Get_Data(feature1,feature2)
            pearson.append(pearsonr(X1,X2)[0])
          
            
            
                        
        accuracy_df = accuracy_df.append({"Feature":features[i],
                                          'DE Ratio':pearson[0],
                               'Trailing P/E':pearson[1],
                               'Price/Sales':pearson[2],
                               'Price/Book':pearson[3],
                               'Profit Margin':pearson[4],
                               'Operating Margin':pearson[5],
                               'Return on Assets':pearson[6],
                               'Return on Equity':pearson[7],
                               'Revenue Per Share':pearson[8],
                               'Market Cap':pearson[9],
                               'Enterprise Value':pearson[10],
                               'Forward P/E':pearson[11],
                               'PEG Ratio':pearson[12],
                               'Enterprise Value/Revenue':pearson[13],
                               'Enterprise Value/EBITDA':pearson[14],
                               'Revenue':pearson[15],
                               'Gross Profit':pearson[16],
                               'EBITDA':pearson[17],
                               'Net Income Avl to Common ':pearson[18],
                               'Diluted EPS':pearson[19],
                               'Earnings Growth':pearson[20],
                               'Revenue Growth':pearson[21],
                               'Total Cash':pearson[22],
                               'Total Cash Per Share':pearson[23],
                               'Total Debt':pearson[24],
                               'Current Ratio':pearson[25],
                               'Book Value Per Share':pearson[26],
                               'Cash Flow':pearson[27],
                               'Beta':pearson[28],
                               'Held by Insiders':pearson[29],
                               'Held by Institutions':pearson[30],
                               'Shares Short (as of':pearson[31],
                               'Short Ratio':pearson[32],
                               'Short % of Float':pearson[33],
                               'Shares Short (prior ':pearson[34]},ignore_index=True)
    accuracy_df.to_csv("pearson.csv")
                        
            
                
    #print(features[i],' ',features[j],':')
    #print("Accuracy:",accuracy)



    



Train_Test()













    
