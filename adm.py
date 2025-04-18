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
      
def year_back(data1:pd.DataFrame,name:str=None):
    #生成年份列表，可添加额外列名。
    year_list = [str(year) for year in range(1980, 2021 + 1)]
    if name != None:
        year_list.append(str(name))        
    return(year_list)
        


def show_result_line(data:pd.DataFrame,name:str):
    Country_list=data.filter(items=["Country"])
    Country_list= Country_list.reset_index(drop=True)
    Country_list["Country"] = Country_list["Country"].str.strip()
    weizhi_list=Country_list[Country_list["Country"] == name].index.tolist()
    weizhi=int(weizhi_list[0])
    print(weizhi)
    linshi=year_back(data,)

    selected_data = data.filter(items=linshi)
    selected_data = selected_data.reset_index(drop=True)
    values = selected_data.iloc[weizhi].tolist()
    data2 = data.filter(items=linshi)
    
    result = {
        '年份': linshi,
        'Value': values
    }
    result1 = pd.DataFrame(result)
    plt_name=Country_list.iloc[0,0]
    plt.figure(figsize=(30, 10))
    sns.lineplot(x='年份', y='Value', data=result1)
    plt.title(plt_name)
    plt.xlabel('year')
    plt.ylabel('value')
    ax = plt.gca()
    ax.invert_yaxis()
    #fig = plt.gcf()
    #fig.savefig('output.png')
    #plt.show()
