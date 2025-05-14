import tkinter as tk

# tk객체 인스턴스 생성하기
root = tk.Tk()
root.title("Label 테스트 화면")
root.geometry("500x500")

# label위젯 생성하기
label1 = tk.Label(root, text="안녕 세상아", font=("Arial", 15), borderwidth=2)
label1.pack()

label2 = tk.Label(root, borderwidth=5, fg="red", text="안녕 세상아2", font=("맑은고딕", 20))
label2.pack()

label3 = tk.Label(root, text="안녕 세상아3", bg="lightyellow", borderwidth=3,font=("명조체", 25))
label3.pack()


txt = ['asdf','asdfa','asdf','asdf','asdfa','asdf']
for t in txt:
    lbl = tk.Label(root, text = t, font=("맑은고딕", 15), fg = 'green')
    lbl.pack()
    
root.mainloop()