# Use the following data for this assignment:

import pandas as pd
import numpy as np

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])

df=df.T
df.columns=df.columns.astype(str)

std=[]
avg=[]
for i in range(1992,1996):
    avg.append(df[str(i)].mean())
    std.append(df[str(i)].std())

from math import *
length=len(df)
conf_lvl_val=1.96

pos=[]
neg=[]
Conf_Int=[]

for i in range(0,4):
    pos.append(avg[i] + (conf_lvl_val*(std[i]/sqrt(length))))
    neg.append(avg[i] - (conf_lvl_val*(std[i]/sqrt(length))))
    Conf_Int.append(pos[i]-neg[i])
    
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap
import matplotlib.pyplot as plt

norm_val=Normalize(vmin=-1.96,vmax=1.96)           #because 'conf_lvl_val=1.96'
cmap=get_cmap('bwr')

new_df=pd.DataFrame(index=[0,1,2,3] , columns=['Value','Color'])

y=int(input("Enter the Y-Value:- "))

for i in range(0,4):
    new_df['Value'][i]=norm_val((avg[i]-y)/std[i])        #formula for data normalization

new_df['Color']= [cmap(x) for x in new_df['Value']]


x=['1992','1993','1994','1995']

plt.bar(x,avg,yerr=Conf_Int,color=new_df['Color'])

plt.axhline(y=y, color='#808080', alpha= 0.5)
plt.text(3.65, y, '%d' %y)
plt.xlabel('Year')
plt.ylabel('Average Votes')
plt.title('Average Votes Vs Year')
