import pandas as pd
import numpy as np
import adm as ad
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'GlobalElectricityStatistics.csv'
column_names = ['col1', 'col2', '']
row_names = ['']
#可能需要去重

data = pd.read_csv(file_path)
num_col=data.columns[3:]
for col in num_col:
    data[col]=pd.to_numeric(data[col],errors="coerce") #coerce返回NAN raise返回异常 ignore忽略

data = data.fillna(0)
#data.to_csv('fix.csv', index=False)

#ad.unique_values_columns(data,'Features')  #找出表中列的唯一值
loss_data=data[data['Features'] == 'distribution losses ']
imports_data=data[data['Features'] == 'imports ']
exports_data=data[data['Features'] == 'exports ']
net_generation_data=data[data['Features'] == 'net generation']

#ad.show_result_line(net_generation_data,"Afghanistan")
#ad.show_result_line(exports_data,"Afghanistan")
#ad.show_result_line(imports_data,"Afghanistan")
#ad.show_result_line(loss_data,"Afghanistan")


#ad.unique_values_columns(loss_data,'Region')
#region_data=ad.unique_value_column_back(loss_data,'Region')
#state_group=loss_data.groupby("Region")
#state_1=state_group.get_group(region_data[0])
#ad.unique_values_columns(data,'Region')
#sum_by_region=state_1[ad.year_back(state_1)[0]].sum()
#mean_by_region=state_1[ad.year_back(state_1)[0]].mean()

#print(ad.mean_year_data(loss_data,1999))


region_data=ad.unique_value_column_back(data,'Region')#从给的dataframe中取独特值
data2=net_generation_data
i1=0
name2="_net_generation"
xuhao="4_"
for i1 in range(0,7):
    name=xuhao+region_data[i1]+name2
    ad.show_result_sum(0,data2,1, "STHeiti",name,i1)

ad.show_result_sum(0,data2,1, "STHeiti",f'{xuhao}global_{name2}')



#ad.show_result_sum(0,imports_data,1, "STHeiti","global_import")
#ad.show_result_sum(0,exports_data,1, "STHeiti","global_export")
#ad.show_result_sum(0,net_generation_data,1, "STHeiti","global_net")
# 字体问题 我一般使用mac编程 所以为 黑体STHeiti 宋体STSong
# 如果为windows 请使用 黑体SimHei 宋体SimSun

