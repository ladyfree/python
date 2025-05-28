import tkinter as tk

root = tk.Tk()
root.title("입력 폼")

labels = ["학년", "반", "번호", "이름", "국어", "수학", "과학"]

for i, label in enumerate(labels):
    tk.Label(root, text= label ).grid(column=0, row=i)
    tk.Entry(root).grid(column=1, row=i)
    
tk.Button(root, text="저장").grid(column=0, row=len(labels))
tk.Button(root, text="초기화").grid(column=1, row=len(labels)) 

root.mainloop()