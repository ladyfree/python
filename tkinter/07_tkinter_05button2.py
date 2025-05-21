import tkinter as tk

def click():
    print(entry1.get())

root = tk.Tk()
root.title("Button Test")

entry1 = tk.Entry(root)
#entry1.pack()
entry1.grid(row=0, column=0)

btn = tk.Button(root, text="클릭", command=click)
#btn.pack()
btn.grid(row=0,column=1)

root.mainloop()