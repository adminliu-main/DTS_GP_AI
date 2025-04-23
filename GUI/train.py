import pandas as pd
import numpy as np
import adm1 as ad
import matplotlib.pyplot as plt
import seaborn as sns
from xgboost import XGBRegressor
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.naive_bayes import GaussianNB
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C, ExpSineSquared



a=4
b=1
data = ad.read_preprocessing('GlobalElectricityStatistics.csv')
years = [str(year) for year in range(1980, 2022)]
years1 = [str(year) for year in range(1980, 2021)]

data=ad.train_data(data)
data=data[data['Country'] == 'United States']
data=data[years]
#print(data)

#test_size = 0.2  # 测试集比例
#data_test = int(42 * test_size)
#train_data = data.iloc[:, :-data_test]
#test_data = data.iloc[:, -data_test:]

test_size = 0.03  # 测试集比例
data_test = int(42 * test_size)
print(data_test)


#data[years] = data[years].astype(float)


train_data = data.iloc[:, :-data_test]
test_data = data.iloc[:, -data_test:]

#years = data.columns.tolist()

#values = data.values.flatten()
years = train_data.columns.tolist()


values = train_data.values.flatten()

X = np.array(years)

y = values



X_train = X
X_train=X_train.astype(float)
X_train=X_train.reshape(-1, 1)
y_train = y

years1 = test_data.columns.tolist()

values = test_data.values.flatten()

X = np.array(years1)

y = values


X_test = X

X_test=X_test.astype(float)
X_test=X_test.reshape(-1, 1)

y_test = y




if a==0:#线性预测

    model = LinearRegression()
    model.fit(X_train, y_train)
    # 评估模型
    X_test = np.array([2024]).reshape(-1, 1)
    prediction_2014 = model.predict(X_test)
    print(f"预测的 2014 年的值为: {prediction_2014[0]}")


if a==1: #XGR



    model = XGBRegressor(
        objective='reg:squarederror',  # 回归任务，使用均方误差作为目标函数
        max_depth=3,  
        learning_rate=0.1,  
        n_estimators=100, 
        colsample_bytree= 0.7,
        subsample= 0.7
)
   
    model.fit(X_train, y_train)
    model.save_model('xgb2.model')
    y_pred = model.predict(X_test)
    print(y_pred)
    print(y_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print(f"均方根误差 (RMSE): {rmse}")
    
    
if a==2: #XGR 网格搜索 自动调参

      
    # 定义参数网格
    param_grid = {
        'learning_rate': [0.01, 0.1, 0.2],
        'n_estimators': [50, 100, 150],
        'subsample': [0.7, 0.8, 0.9],
        'colsample_bytree': [0.7, 0.8, 0.9],  
        'max_depth': [3, 5, 7]
        }

    model = xgb.XGBRegressor(objective='reg:squarederror')

    # 创建网格搜索对象
    grid_search = GridSearchCV(model, param_grid, cv=3, scoring='neg_mean_squared_error', verbose=2)

    grid_search.fit(X_train, y_train)

    print("最佳参数:", grid_search.best_params_)


if a==3: #朴素贝叶斯
    model = GaussianNB()
    print(y_train)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(y_pred)
    print(y_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print(f"均方根误差 (RMSE): {rmse}")



if a==4: #XGR

    loaded_model = xgb.XGBRegressor()
    loaded_model.load_model('xgb2.model')
    for year in range(2001, 2010):
        X_test = np.array([year]).reshape(-1, 1)
        y_pred = loaded_model.predict(X_test)
        print(f"{year} 年的预测值为: {y_pred[0]}")

    
  