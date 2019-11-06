#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 00:53:22 2019

@author: dipanshu
"""

import pandas as pd
import numpy as np
from matplotlib.pyplot import boxplot
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def remove_outlier(df_in, col_name):
    q1 = df_in[col_name].quantile(0.25)
    q3 = df_in[col_name].quantile(0.75)
    iqr = q3-q1 #Interquartile range
    fence_low  = q1-1.5*iqr
    fence_high = q3+1.5*iqr
    df_out = df_in.loc[(df_in[col_name] > fence_low) & (df_in[col_name] < fence_high)]
    return df_out

path = '/home/dipanshu/Desktop/IITMandi/semester_3/DataScience3/Mini-project_DataScience3/data/correalted_dropped_data.csv'

corr_corrected_data = pd.read_csv(path)

#reduced_data = PCA(n_components=2).fit_transform(corr_corrected_data)
cols = corr_corrected_data.columns

for i in cols:
    boxplot(corr_corrected_data[i])
    plt.title(i)
    plt.savefig('/home/dipanshu/Desktop/IITMandi/semester_3/DataScience3/Mini-project_DataScience3/data_cleaning/graphs/'+str(i)+str('rem_corr_cols.jpeg'))    
    
