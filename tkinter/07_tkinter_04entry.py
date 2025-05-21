import tkinter as tk

def on_submit():
    user_input = entry1.get()
    print("입력한 내용:", user_input)
    entry1.delete(0, tk.END)  # 입력창 비우기


root = tk.Tk()
root.title("Entry Test")

entry1 = tk.Entry(root, width=10, font=("맑은 고딕", 12), fg="yellow", bg="green")
entry1.pack()

# 버튼 위젯
btn = tk.Button(root, text="제출", command=on_submit)
btn.pack()

root.mainloop()
