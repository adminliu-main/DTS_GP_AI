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