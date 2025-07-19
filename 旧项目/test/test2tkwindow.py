import tkinter as tk

# 创建第一个窗口
window1 = tk.Tk()
window1.title("窗口 1")
window1.geometry("300x200")

label1 = tk.Label(window1, text="这是窗口 1")
label1.pack()

# 创建第二个窗口
window2 = tk.Tk()
window2.title("窗口 2")
window2.geometry("300x200")

label2 = tk.Label(window2, text="这是窗口 2")
label2.pack()

# 运行主循环
window1.mainloop()
window2.mainloop()
