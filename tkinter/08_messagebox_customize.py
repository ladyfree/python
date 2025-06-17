import tkinter as tk
from tkinter import messagebox  # messagebox 모듈 가져오기

def show_info():
    messagebox.showinfo("안내", "이것은 정보성 메시지입니다.")

def show_warning():
    messagebox.showwarning("경고", "이 작업은 주의가 필요합니다!")

def show_error():
    messagebox.showerror("오류", "오류가 발생했습니다.")

def ask_yes_no():
    answer = messagebox.askyesno("확인", "계속 진행하시겠습니까?")
    if answer:
        print("사용자: 예")
    else:
        print("사용자: 아니오")
        
root = tk.Tk()

btn1 = tk.Button(root, text="정보창 띄우기", command=show_info)
btn1.pack(pady=10)
btn1 = tk.Button(root, text="경고창 띄우기", command=show_warning)
btn1.pack(pady=10)
btn1 = tk.Button(root, text="오류창 띄우기", command=show_error)
btn1.pack(pady=10)
btn1 = tk.Button(root, text="예/아니요 묻기 ", command=ask_yes_no)
btn1.pack(pady=10)

root.mainloop()