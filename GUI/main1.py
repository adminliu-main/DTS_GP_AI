import pandas as pd
import numpy as np
import adm1 as ad
import matplotlib.pyplot as plt
import seaborn as sns

data = ad.read_preprocessing('GlobalElectricityStatistics.csv')
loss_data=data[data['Features'] == 'distribution losses ']
imports_data=data[data['Features'] == 'imports ']
exports_data=data[data['Features'] == 'exports ']
net_generation_data=data[data['Features'] == 'net generation']
selected_countries = ['China', 'United States', 'India', 'Russia', 'Japan']
a =1
#ad.year_chart(data,selected_countries,'distribution losses')
#ad.year_chart(data,selected_countries)
#ad.year_chart(data,selected_countries)
#ad.year_chart(data,selected_countries)

#data1=ad.mean_year_data(net_generation_data,2000,2021)[0]
#selected_data = data1[data1['Country'].isin(selected_countries)]
#ad.plt_showbar(selected_data,selected_countries,(12,6),"2000 - 2021 年选定国家平均年发电量比较","国家","平均年发电量")

#max_avg_country = data1.loc[data1['Average Generation'].idxmax()]
#min_avg_country = data1.loc[data1['Average Generation'].idxmin()]

#print("\n该时期最高平均发电量的国家：")
#print(max_avg_country[['Country', 'Average Generation']])
#print("\n该时期最低平均发电量的国家：")
#print(min_avg_country[['Country', 'Average Generation']])
data1=ad.reattach(data)
max_avg_country = data1.loc[data1['Average net consumption'].idxmax()]
min_avg_country = data1.loc[data1['Average net consumption'].idxmin()]

print("\n该时期最高平均净消费量的国家：")
print(max_avg_country[['Country', 'Average net consumption']])
#print("\n该时期最低平均净消费量的国家：")
#print(min_avg_country[['Country', 'Average net consumption']])

#ad.mean_year_data(net_generation_data,2000,2021)[0].to_csv('test1.csv', index=False)
#print(len(data1))
#train_size = int(len(data1) * 0.8)
#print(train_size)
#train = data1[:train_size]
#test = data1[train_size:]
#train.to_csv('train.csv', index=False)
#test.to_csv('test.csv', index=False)
#ad.train_data(data).to_csv('train.csv', index=False)




    