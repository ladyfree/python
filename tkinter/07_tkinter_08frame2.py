import tkinter as tk

root = tk.Tk()
root.title("심플 Frame 예제")

# 1) 빈 Frame 생성
frame1 = tk.Frame(root, relief="groove", bd=2, bg="skyblue")
frame1.pack(side="left", fill="both", expand=True, padx=10)
frame2 = tk.Frame(root, relief="solid", bd=2)
frame2.pack(side="right",fill="both", expand=True)

lbl1 = tk.Label(frame1, text="hello1")
lbl1.pack()
lbl2 = tk.Label(frame2, text="hello2")
lbl2.pack()



root.mainloop()