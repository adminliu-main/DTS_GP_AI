import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
control_file="language.txt"
initialized = False

class EmptyDataFrameError(Exception):
    pass

def initialize(file_path:str):
    global language
    new=[]
    try:    
        file = open(control_file, 'r', encoding='utf-8')
        linshi = file.readlines()
        file.close
        
        for linshi1 in linshi:
            new1=linshi1.replace("\n",'')
            key, value = new1.split('=')
            new.append([key,value])
        language=int(new[0][1])
    except FileNotFoundError:
        print("发生错误：未找到指定的语言文件")
        try:
            with open(control_file,"w",encoding="utf-8") as file:
                list=["language=1"]
                content="\n".join(list)
                file.write(content)
                language=1
            print("已自动新建，默认为英文。")
        except Exception as e:
            print(f"写入文件时出现错误:{e}")

def singleton_init(ininialize):
    init_result = None
    initialized = False
    def wrapper():
        nonlocal init_result, initialized
        if not initialized:
            print("进行初始化操作")
            init_result = ininialize()
            initialized = True
        return init_result
    return wrapper

def aprint(contents:str):
    global language
    if language==1:
        print(f"Error：{contents}")
    if language==0:
        print(f"发生错误：{contents}")
    
def unique_value_column_back(data:pd.DataFrame,name:str):
    if not name:
        print("提供的列名为空")
        print("列名:",data.columns)
    if name in data.columns:
        unique_values = data[name].unique()
        return(unique_values)
    else:
        print("在DataFrame中找不到该列")
        print("列名:",data.columns)

def read_preprocessing(file_path:str):
    initialize(file_path)
    try:
        data = pd.read_csv(file_path)

        num_col=data.columns[3:]
        for col in num_col:
            data[col]=pd.to_numeric(data[col],errors="coerce") 
            #coerce返回NAN raise返回异常 ignore忽略
        data = data.fillna(0)
        for i in data.head(0).columns[:3]:
            data[i] = data[i].str.strip()
        return(data)
    except EmptyDataFrameError as e:
        aprint(e)
    except FileNotFoundError as e:
        aprint(e)
    except Exception as e:
        aprint(e)

def years1():
    years = [str(year) for year in range(1980, 2022)]
    return(years)

def years2(start:int,stop:int):
    years = [str(year) for year in range(start, stop+1)]
    return(years)
   
def year_chart(data:pd.DataFrame,selected_countries:list,selected_features:str):
    years=years1()
    data=data[data['Features'] == selected_features]
    selected_data = data[data['Country'].isin(selected_countries)][['Country'] + years]
    title_name=selected_features.capitalize()+" Trend (1980-2021)"
    plt_show(selected_data,years,(12,6),title_name,"Years",selected_features.capitalize())

def year_chartbar(data:pd.DataFrame,selected_countries:list,years):
    #data=data[data['Features'] == selected_features]
    selected_data = data[data['Country'].isin(selected_countries)][['Country'] + years]
    title_name=" Trend (1980-2021)"
    plt_showbar(selected_data,years,(12,6),title_name,"Years","Value")


def plt_show(data:pd.DataFrame,x_data:list,figsize1,title:str,x_name:str,y_name:str):
    plt.figure(figsize=figsize1)

    # 绘制每个国家的折线图
    for index, row in data.iterrows():
        country = row['Country']
        plt.plot(x_data, row[x_data], label=country)

    # 添加标题、标签和图例
    plt.title(title)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.legend()

    # 设置 x 轴标签旋转角度
    plt.xticks(rotation=45)

    # 显示图形
    plt.show()

def plt_showbar(data:pd.DataFrame,x_data:list,figsize1,title:str,x_name:str,y_name:str):
    plt.figure(figsize=figsize1)
    ziti = 'STHeiti'
    plt.rcParams['font.family'] = ziti
    plt.bar(data['Country'], data['Average Generation'])

    # 添加标题、标签和图例
    plt.title(title)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.legend()

    # 设置 x 轴标签旋转角度

    # 显示图形
    plt.show()

def mean_year_data(data:pd.DataFrame,year_start:int,year_stop:int,region_num:int=None,region:str=None):
    data1=[]
    data2=[]
    data2 = pd.DataFrame(data2)
    years=years2(year_start,year_stop)
    data1 = data[['Country'] + years]
    data2['Country']=data['Country'] 
    data2['Average'] = data1[years].mean(axis=1)

    return(data2,years)

def reattach(data:pd.DataFrame):
    years=years2(1980,2021)
    #data = data[['Country'] +['Features']+['Region']+ years]
    result=0
    grouped = data.groupby('Country') #按照国家分组
    new = pd.DataFrame(columns=data.columns)
    for country, group in grouped: 
        new = pd.concat([new, group], ignore_index=True)
        net_consumption=pd.DataFrame()
        new_df = pd.DataFrame()
        last_columns = group.iloc[2:, :]
        new_df = pd.concat([new_df, last_columns], axis=1)
        net_consumption = pd.DataFrame(columns=new_df.columns)
        net_consumption.at[1, 'Features'] = 'net consumption'
        net_consumption.at[1, 'Country'] = country
        net_consumption.at[1, 'Region'] = group['Region'].reset_index(drop=True)[0]
        loss_data=group[group['Features'] == 'distribution losses'].reset_index(drop=True)
        imports_data=group[group['Features'] == 'imports'].reset_index(drop=True)
        exports_data=group[group['Features'] == 'exports'].reset_index(drop=True)
        net_generation_data=group[group['Features'] == 'net generation'].reset_index(drop=True)
        new['Average'] = new[years].mean(axis=1)
        for i in range(1,43):
            year_cols=str(i+1979)
            result =  net_generation_data[year_cols] + imports_data[year_cols] - exports_data[year_cols] - loss_data[year_cols]
            net_consumption.at[1, year_cols] = result.values
        net_consumption['Average net consumption'] = net_consumption[years].mean(axis=1)
        

        
        new = pd.concat([new, net_consumption], ignore_index=True)


    return(new)
 
def train_data(data:pd.DataFrame):
    years=years2(1980,2021)
    result=0
    grouped = data.groupby('Country') #按照国家分组
    new = pd.DataFrame(columns=data.columns)
    for country, group in grouped: 
        net_consumption=pd.DataFrame()
        new_df = pd.DataFrame()
        last_columns = group.iloc[2:, :]
        new_df = pd.concat([new_df, last_columns], axis=1)
        net_consumption = pd.DataFrame(columns=new_df.columns)
        net_consumption.at[1, 'Features'] = 'net consumption'
        net_consumption.at[1, 'Country'] = country
        net_consumption.at[1, 'Region'] = group['Region'].reset_index(drop=True)[0]
        loss_data=group[group['Features'] == 'distribution losses'].reset_index(drop=True)
        imports_data=group[group['Features'] == 'imports'].reset_index(drop=True)
        exports_data=group[group['Features'] == 'exports'].reset_index(drop=True)
        net_generation_data=group[group['Features'] == 'net generation'].reset_index(drop=True)
        for i in range(1,43):
            year_cols=str(i+1979)
            result =  net_generation_data[year_cols] + imports_data[year_cols] - exports_data[year_cols] - loss_data[year_cols]
            net_consumption.at[1, year_cols] = result.values
        

        
        new = pd.concat([new, net_consumption], ignore_index=True)


    return(new)


def reattach_odddd(data:pd.DataFrame):
    years=years2(1980,2021)
    result=0
    grouped = data.groupby('Country') #按照国家分组
    new = pd.DataFrame(columns=data.columns)
    for country, group in grouped: 
        new = pd.concat([new, group], ignore_index=True)
        net_consumption=pd.DataFrame()
        new_df = pd.DataFrame()
        last_columns = group.iloc[2:, :]
        new_df = pd.concat([new_df, last_columns], axis=1)
        net_consumption = pd.DataFrame(columns=new_df.columns)
        net_consumption.at[1, 'Features'] = 'net_consumption'
        loss_data=group[group['Features'] == 'distribution losses'].reset_index(drop=True)
        imports_data=group[group['Features'] == 'imports'].reset_index(drop=True)
        exports_data=group[group['Features'] == 'exports'].reset_index(drop=True)
        net_generation_data=group[group['Features'] == 'net generation'].reset_index(drop=True)
        new['Average'] = new[years].mean(axis=1)
        for i in range(1,43):
            year_cols=str(i+1979)
            result =  net_generation_data[year_cols] + imports_data[year_cols] - exports_data[year_cols] - loss_data[year_cols]
            net_consumption.at[1, year_cols] = result.values
        new['Average net consumption'] = net_consumption[years].mean(axis=1)
        


    return(new)

