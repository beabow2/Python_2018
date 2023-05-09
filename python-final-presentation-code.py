# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 16:42:16 2018

@author: User
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import statsmodels as st
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats

# 第一張圖
path='D:/Downloads/Python/python_final_presentation/'
isocode_list = ['AUS','BRA','CAN','GER','FRA','ICE','ITA','JAP','MEX','ROK','SIN','SA','SWE','UK','US']
x_axis = ['5~14', '15~24', '25~34', '35~54', '55~74', '75+']
N0 = len(isocode_list)
X = N0*[None]
Y = N0*[None]
for ii in range(N0):
    X[ii] = pd.read_excel(path+'15country_fig1.xlsx', sheet_name=isocode_list[ii], header=0, index_col=0) 
    X[ii].index = x_axis
    
fig1, axes= plt.subplots(N0,1)
for ii in range(N0):
    x = X[ii].index
    y = X[ii].T.values
    labels = X[ii].columns
    for i in range(len(labels)):
        axes[ii].plot(x, y[i], label=labels[i])
        axes[ii].set_xlabel('Age', fontsize=20)
        axes[ii].set_ylabel('suicide rate ‰', fontsize=20)
        axes[ii].tick_params(axis='both', labelsize=20)
        axes[ii].set_title(isocode_list[ii], fontsize=20)
        fig1.set_size_inches(15,120)
        axes[ii].legend()
'''plt.savefig('D:/Users/User/Desktop/python/python_final_presentation/country.png',dpi=400,bbox_inches='tight')'''
plt.show()


# 第二張圖
isocode_list = ['2007','2008','2009']
N0 = len(isocode_list)
Y = N0*[None]
for jj in range(N0):
    Y[jj] = pd.read_excel(path+'15country_fig2_data.xlsx', sheet_name=isocode_list[jj], header=0, index_col=0) 
    Y[jj] = Y[jj]

fig1, axes= plt.subplots(N0,1)
for jj in range(N0):
    x = Y[jj].index
    y = Y[jj].T.values
    labels = Y[jj].columns
    for j in range(len(labels)):
        axes[jj].plot(x, y[j], label=labels[j])
    axes[jj].set_xlabel('Age', fontsize=20)
    axes[jj].set_ylabel('suicide rate ‰', fontsize=20)
    axes[jj].tick_params(axis='both', labelsize=20)
    axes[jj].set_title(isocode_list[jj], fontsize=20)
    fig1.set_size_inches(25, 30)
    axes[jj].legend()
'''plt.savefig('C:/Users/智晴/Desktop/python/python_final_presentation/year.png',dpi=400,bbox_inches='tight')'''
plt.show()

#匯入全部資料
suicide = pd.read_excel(path+'suiciderate.xlsx',header = 0)
suicide.head()
#匯入各sheet
suicide_2007=pd.read_excel(path+'suiciderate.xlsx',sheet_name='2007',header = 0)
suicide_2007.head()
suicide_2008=pd.read_excel(path+'suiciderate.xlsx',sheet_name='2008',header = 0)
suicide_2008.head()
suicide_2009=pd.read_excel(path+'suiciderate.xlsx',sheet_name='2009',header = 0)
suicide_2009.head()

"""2007"""
#將性別改為Dummy variable
suicide_2007['gender_D'] = suicide_2007.gender.map({'female':0,'male':1})
#去除變數
suicide_2007 = suicide_2007.drop(['suicides_no','population','gender'],axis=1)
#做ols迴歸分析
reg_2007=smf.ols('rate~gender_D+GDP',data = suicide_2007).fit()
print(reg_2007.summary())

"""2008"""
#將性別改為Dummy variable
suicide_2008['gender_D'] = suicide_2008.gender.map({'female':0,'male':1})
#去除變數
suicide_2008 = suicide_2008.drop(['suicides_no','population','gender'],axis=1)
#做ols迴歸分析
reg_2008=smf.ols('rate~gender_D+GDP',data = suicide_2008).fit()
print(reg_2008.summary())

"""2009"""
#將性別改為Dummy variable
suicide_2009['gender_D'] = suicide_2009.gender.map({'female':0,'male':1})
#去除變數
suicide_2009 = suicide_2009.drop(['suicides_no','population','gender'],axis=1)
#做ols迴歸分析
reg_2009=smf.ols('rate~gender_D+GDP',data = suicide_2009).fit()
print(reg_2009.summary())

#比較三年之間的自殺率有無顯著不同
'''rate_2007 = suicide_2007['rate']
rate_2008 = suicide_2008['rate']
rate_2009 = suicide_2009['rate']

result1 = st.stats.weightstats.ttest_ind(rate_2007, rate_2008,alternative='two-sided')
print(result1)
result2 = st.stats.weightstats.ttest_ind(rate_2008, rate_2009,alternative='two-sided')
print(result2)
result3 = st.stats.weightstats.ttest_ind(rate_2007, rate_2009,alternative='two-sided')
print(result3)'''


rate_2007 = suicide_2007['rate']
rate_2008 = suicide_2008['rate']
rate_2009 = suicide_2009['rate']
result4=stats.ttest_rel(rate_2008,rate_2007)
print(result4)
result5=stats.ttest_rel(rate_2009,rate_2008)
print(result5)
result6=stats.ttest_rel(rate_2009,rate_2007)
print(result6)