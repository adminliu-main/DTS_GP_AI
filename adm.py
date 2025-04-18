import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class EmptyDataFrameError(Exception):
    pass

def jiancha(data1:pd.DataFrame):
    #检查提供的DataFrame是否为空，如果为空报错
    data=pd.DataFrame(data1)
    if isinstance(data, pd.DataFrame) and data.empty:
        raise EmptyDataFrameError("提供的 pandas.core.frame.DataFrame 为空")
    return(data)

def unique_values_columns(data1:pd.DataFrame,name:str):
    data=jiancha(data1)
    # 检测 参数name 是否为空
    if not name:
        print("提供的列名为空")
        print("列名:",data.columns)
    if name in data.columns:
        unique_values = data[name].unique()
        print("列的唯一值：", unique_values)
    else:
        print("在DataFrame中找不到该列")
        print("列名:",data.columns)

def unique_value_column_back(data1:pd.DataFrame,name:str):
    data=jiancha(data1)
    # 检测 参数name 是否为空
    if not name:
        print("提供的列名为空")
        print("列名:",data.columns)
    if name in data.columns:
        unique_values = data[name].unique()
        return(unique_values)
    else:
        print("在DataFrame中找不到该列")
        print("列名:",data.columns)

def year_back(data1:pd.DataFrame,name:str=None):
    #生成年份列表，可添加额外列名。
    year_list = [str(year) for year in range(1980, 2021 + 1)]
    if name != None:
        year_list.append(str(name))        
    return(year_list)
        

def show_result_line(data:pd.DataFrame,name:str,title_name:str=None,X_name:str=None,Y_name:str=None,x_size:int=None,y_size:int=None):
    data['Country'] = data['Country'].str.strip()
    data = data.reset_index(drop=True)
    country_indices = data[data['Country']== name].index
    if country_indices.empty:
        print("未找到名为{name}的国家数据")
        return
    weizhi=int(country_indices[0])
    print()
    linshi=year_back(data,)

    selected_data = data.filter(items=linshi)
    selected_data = selected_data.reset_index(drop=True)
    values = selected_data.iloc[weizhi].tolist()
    data2 = data.filter(items=linshi)
    
    result = {
        'x': linshi,
        'y': values
    }
    result1 = pd.DataFrame(result)

    if x_size==None:
        x_size=30
    if y_size==None:
        y_size=10
    plt.figure(figsize=(x_size, y_size))
    sns.lineplot(x='x', y='y', data=result1)
    if title_name==None:
        title_name=name
    plt.title(title_name)
    if X_name==None:
        X_name="Year"
    plt.xlabel(X_name)
    if Y_name==None:
        Y_name="value"
    plt.ylabel(Y_name)
    ax = plt.gca()
    ax.invert_yaxis()
    #fig = plt.gcf()
    #fig.savefig('output.png')
    plt.show()


def sum_year_data(data:pd.DataFrame,year1:int=None,region_num:int=None,region:str=None):
    region_data=unique_value_column_back(data,'Region')#从给的dataframe中取独特值
    state_group=data.groupby("Region")#按照地区分组
    if region == None:
        if region_num==None:
            region_num=0
    state_1=state_group.get_group(region_data[region_num])#取出需要的地区的相关表   
    year_num=year_back(state_1)
    year_num_series = pd.Series(year_num)
    #print(year_num_series)
    year=str(year1)
    if year1 is None:
        year=str(year_num[0])
    if not year_num_series.isin([year]).any() :
        print("给出的年份不在列表中")
        return
    sum_by_region=state_1[year].sum()
    return(sum_by_region)
    #mean_by_region=state_1[year_back(state_1)[0]].mean()


def mean_year_data(data:pd.DataFrame,year1:int=None,region_num:int=None,region:str=None):
    region_data=unique_value_column_back(data,'Region')#从给的dataframe中取独特值
    state_group=data.groupby("Region")#按照地区分组
    if region == None:
        if region_num==None:
            region_num=0
    state_1=state_group.get_group(region_data[region_num])#取出需要的地区的相关表   
    year_num=year_back(state_1)
    year_num_series = pd.Series(year_num)
    #print(year_num_series)
    year=str(year1)
    if year1 is None:
        year=str(year_num[0])
    if not year_num_series.isin([year]).any() :
        print("给出的年份不在列表中")
        return
    mean_by_region=state_1[year].mean()
    return(mean_by_region)
    