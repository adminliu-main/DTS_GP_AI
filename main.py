import pandas as pd
import numpy as np
import adm as ad
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'GlobalElectricityStatistics.csv'
column_names = ['col1', 'col2', '']
row_names = ['']
#可能需要去重

data = pd.read_csv(file_path,na_values=['--'])
data_filled_with_zero = data.fillna(0)

#ad.unique_values_columns(data,'Features')  #找出表中列的唯一值
loss_data=data[data['Features'] == 'distribution losses ']
imports_data=data[data['Features'] == 'imports ']
exports_data=data[data['Features'] == 'exports ']
net_generation_data=data[data['Features'] == 'net generation']

ad.show_result_line(net_generation_data,"Afghanistan")
#ad.show_result_line(exports_data,"Afghanistan")
#ad.show_result_line(imports_data,"Afghanistan")
#ad.show_result_line(loss_data,"Afghanistan")


