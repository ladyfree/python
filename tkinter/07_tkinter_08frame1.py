import tkinter as tk

root = tk.Tk()
root.title("frame exam")

# frame선언
frame1 = tk.Frame(root)
frame1.pack(pady=10)

# 버튼
btn = tk.Button(root, text="버튼1")
btn.pack()
btn = tk.Button(frame1, text="버튼2")
btn.pack()
btn = tk.Button(frame1, text="버튼3")
btn.pack()
btn = tk.Button(frame1, text="버튼4")
btn.pack()


root.mainloop()