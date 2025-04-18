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
num_col=data.columns[2:]
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



#region_data=ad.unique_value_column_back(loss_data,'Region')
#state_group=loss_data.groupby("Region")
#state_1=state_group.get_group(region_data[0])

#sum_by_region=state_1[ad.year_back(state_1)[0]].sum()
#mean_by_region=state_1[ad.year_back(state_1)[0]].mean()
print(ad.sum_year_data(loss_data,1999))
print(ad.mean_year_data(loss_data,1999))