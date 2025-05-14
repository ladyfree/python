import tkinter as tk  # tkinter 라이브러리 불러오기

# 1. 기본 창(root) 생성
root = tk.Tk()
root.title("Tkinter 기본 구조")  # 창 제목 설정

# 2. 라벨(Label) 추가
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()  # pack()을 사용하여 화면에 배치

# 3. 버튼(Button) 추가
def on_click():
    label.config(text="버튼이 클릭됨!")  # 라벨 텍스트 변경

button = tk.Button(root, text="클릭하세요", command=on_click)
button.pack()

# 4. GUI 실행
root.mainloop()