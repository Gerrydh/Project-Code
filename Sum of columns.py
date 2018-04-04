import pandas as pd 
import numpy as np
import scipy as sp 
import matplotlib as mpl 
import seaborn as sns

df = pd.read_csv("iris head.csv")

print(sum(df['Sepal Length']))
print(sum(df['Sepal Width']))
print(sum(df['Petal length']))
print(sum(df['Petal Width']))
