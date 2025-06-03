import tkinter as tk

root = tk.Tk()
root.title("Frame Example")
root.geometry("300x200")

frame1=tk.Frame(root, relief="solid", bd=2)
frame1.pack(side="left", fill="both", expand=True)
# frame3=tk.Frame(root, bg="yellow", width=1)
# frame3.pack(side="left", fill="both", expand=True)
frame2=tk.Frame(root, relief="solid", bd=2)
frame2.pack(side="right", fill="both", expand=True)

lbl1 = tk.Button(frame1, text="프레임1")
lbl1.pack(side="right")
lbl2 = tk.Button(frame2, text="프레임2")
lbl2.pack(side="bottom")

root.mainloop()