   
def net_ele_gen_trend(data:pd.DataFrame,selected_countries:list,):
    data = ad.read_preprocessing('GlobalElectricityStatistics.csv')
    years=years1()
    loss_data=data[data['Country'] == 'China']
    data=data[data['Features'] == 'net generation']
    selected_data = data[data['Country'].isin(selected_countries)][['Country'] + years]
# 选择 5 个国家 #



selected_countries = ['China', 'United States', 'India', 'Russia', 'Japan']



 
# 筛选出 1980 - 2021 年的数据

#print(loss_data)
# 提取所选国家的数据


# 设置图形大小
plt.figure(figsize=(12, 6))

# 绘制每个国家的折线图
for index, row in selected_data.iterrows():
    country = row['Country']
    plt.plot(years, row[years], label=country)

# 添加标题、标签和图例
plt.title('Net Electricity Generation Trend (1980 - 2021)')
plt.xlabel('Year')
plt.ylabel('Net Electricity Generation')
plt.legend()

# 设置 x 轴标签旋转角度
plt.xticks(rotation=45)

# 显示图形
plt.show()
