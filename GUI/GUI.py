import tkinter as tk
from tkinter import filedialog

# 创建主窗口
root = tk.Tk()
root.title('DTS002TC-Group-AI')

label = tk.Label(root, text='欢迎使用！')
label.pack(pady=20)

entry = tk.Entry(root,width=40)
entry.pack(pady=10)

def button_clicked():
    text = entry.get()
    print(f'你输入的内容是：{text}')

button = tk.Button(root, text='点击我', command=button_clicked)
button.pack(pady=10)

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

file_button = tk.Button(root, text='选择文件', command=select_file)
file_button.pack(pady=10)

root.mainloop()



# 假设你要预测的目标列是 'target'，特征列是除 'target' 之外的列
X = data.drop('target', axis=1)
y = data['target']

# 按照时间顺序拆分数据，80% 为训练集，20% 为测试集
train_size = int(len(X) * 0.8)
X_train = X[:train_size]
X_test = X[train_size:]
y_train = y[:train_size]
y_test = y[train_size:]

print("训练集特征数据:")
print(X_train)
print("训练集目标数据:")
print(y_train)
print("测试集特征数据:")
print(X_test)
print("测试集目标数据:")
print(y_test)