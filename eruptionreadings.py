# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 13:42:16 2018

@author: ankit
"""

from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv(r"eruptionreadings.csv")
print(df.head())
f1 = df['Eruption'].values
f2 = df['Waiting_time'].values
X = np.array(list(zip(f1, f2)))
plt.scatter(f1, f2, c='green', s=7)
plt.show()