import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm,preprocessing
import pandas as pd
from matplotlib import style
import time
from sklearn.model_selection import GridSearchCV

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
    data_df = data_df.replace('N/A',0)
    data_df = data_df.fillna(0)

    data_df = data_df.reindex(np.random.permutation(data_df.index))
    
    X = np.array(data_df[features].values)
    y = np.array(data_df["Status"].replace("outperform",1).replace("underperform",0).values)
       
    X_mean = X.mean(axis=0)
    X_std = X.std(axis=0)
    X = (X-X_mean)/X_std

    
    return X,y



def Parameter_adjust():
    
    vote10 = 0
    vote11 = 0
    vote12 = 0
    vote13 = 0
    vote14 = 0
    vote15 = 0
    
    
    
    for i in range(50):
        X,y = Get_Data()
        grid = GridSearchCV(svm.SVC(),
                            param_grid={"C":[10,11,12,13,14,15],
                                        "gamma":[1]},
                            cv=6)
        grid.fit(X,y)
        
        if grid.best_params_["C"] == 10:
            vote10+=1
        elif grid.best_params_["C"] == 11:
            vote11+=1
        elif grid.best_params_["C"] == 12:
            vote12+=1
        elif grid.best_params_["C"] == 13:
            vote13+=1
        elif grid.best_params_["C"] == 14:
            vote14+=1
        elif grid.best_params_["C"] == 15:
            vote15+=1
        
        
            

    #print("Best parameter is: ", grid.best_params_)
    #print("Best score is: ", grid.best_score_)
    print("vote10= ",vote10)
    print("vote11= ",vote11)
    print("vote12= ",vote12)
    print("vote13= ",vote13)
    print("vote14= ",vote14)
    print("vote15= ",vote15)
    
    

        
Parameter_adjust()










    
