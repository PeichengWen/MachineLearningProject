import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm,preprocessing
import pandas as pd
from matplotlib import style
import time
from sklearn.model_selection import GridSearchCV

style.use("ggplot")


features = ['DE Ratio',
                        'Profit Margin',
                        'Operating Margin',
                        'Diluted EPS',
                        'Net Income Avl to Common ',
                        'EBITDA',
                        'Total Cash',
                        'Price/Sales',
                        'Enterprise Value',
                        'Return on Assets']


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
    
    
    
    
    
    for i in range(50):
        X,y = Get_Data()
        grid = GridSearchCV(svm.SVC(),
                            param_grid={"C":[50,100,150,200],
                                        "gamma":[5,10,15]},
                            cv=6)
        grid.fit(X,y)
        
        
        
        
            

    print("Best parameter is: ", grid.best_params_)
    print("Best score is: ", grid.best_score_)
    
    
    

        
Parameter_adjust()










    
