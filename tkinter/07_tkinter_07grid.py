import tkinter as tk

root = tk.Tk()
root.title("그리드 테스트")

for i in range(3):
    tk.Button(root, text="버튼").pack()
    
for i in range(3):
    tk.Button(root, text="버튼").grid(column=i+1, row=1, padx=3)

root.mainloop()