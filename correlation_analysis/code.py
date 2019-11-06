"""
    MINI PROJECT 
    SEMESTER 3
    Dipanshu Verma
    
"""

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler,MinMaxScaler

data =  pd.read_csv('Batch04.csv')

corr_matrix = data.corr().abs()

upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))
to_drop = [column for column in upper.columns if any(upper[column] > 0.90)]

dropped_data = data.drop(data[to_drop],axis=1,inplace=False)

dropped_data.to_csv('dropped_data.csv')