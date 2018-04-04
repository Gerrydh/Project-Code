import pandas as pd 
import numpy as np
import scipy as sp 
import matplotlib as mpl 
import seaborn as sns

df = pd.read_csv("iris head.csv")


df.describe(include=['object'])
print(min(df.sum(axis=1)))
print(max(df.sum(axis=1)))
