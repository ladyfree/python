import tkinter as tk

def click():
    print("버튼을 눌렀어요")

root = tk.Tk()
root.title("Button Test")

btn = tk.Button(root, text="클릭", command=click)
btn.pack()

root.mainloop()