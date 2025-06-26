import tkinter as tk
from PIL import Image, ImageTk
import random
import os

# 설정
IMAGE_FOLDER = "tarot"
canvas_width = 800
canvas_height = 500

# Tkinter 설정
root = tk.Tk()
root.title("웨이트 타로 읽기 연습용")

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

text = tk.Text(root, font=("맑은 고딕", 14), width=70, height= 3)

card_images = []      # 카드 이미지 참조 유지
tarot_image = []      # 카드 이름 리스트
questions = []        # 질문 리스트

# 이미지 폴더에서 카드 목록 불러오기
def load_tarot_images():
    global tarot_image
    files = os.listdir(IMAGE_FOLDER)
    tarot_image = [
        os.path.splitext(f)[0]
        for f in files
        if f.lower().endswith(".jpg")
    ]

# 질문 파일에서 질문 목록 불러오기
def load_questions():
    global questions
    path = os.path.join(IMAGE_FOLDER, "question.txt")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            questions = [line.strip() for line in f if line.strip()]

# 카드 3장과 질문을 보여주는 함수
def draw_cards():
    canvas.delete("all")
    card_images.clear()
    text.delete("1.0", tk.END)

    if len(tarot_image) < 3:
        print("카드 이미지가 3장 이상 있어야 합니다.")
        return

    selected_cards = random.sample(tarot_image, 3)
    #print("뽑힌 카드:", selected_cards)

    # 질문 표시
    if questions:
        question = random.choice(questions)
        canvas.create_text(canvas_width // 2, 80, text="질문 : "+question, font=("맑은 고딕", 16, "bold"), fill="blue")

    # 카드 표시
    for i, name in enumerate(selected_cards):
        path = os.path.join(IMAGE_FOLDER, f"{name}.jpg")
        img = Image.open(path).resize((250, 350))
        photo = ImageTk.PhotoImage(img)
        card_images.append(photo)
        canvas.create_image(140 + i * 260, 320, image=photo)  # 아래쪽에 위치

# 버튼 생성
btn = tk.Button(root, text="타로카드 뽑기", command=draw_cards, font=("맑은 고딕", 14))
btn.pack(pady=10)


text.pack(pady=10)

# 초기 데이터 로딩
load_tarot_images()
load_questions()

root.mainloop()
