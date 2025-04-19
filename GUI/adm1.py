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
