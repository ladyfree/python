import tkinter as tk

root = tk.Tk()
root.title("Label Bitmap 예제")

bitmaps = ["error", "info", "question", "warning", "hourglass", "gray75", "gray50", "gray25", "gray12", "questhead"]

for bm in bitmaps:
    lbl = tk.Label(root,
                   text=bm,
                   bitmap=bm,        # 내장 비트맵 지정
                   compound="right",  # 이미지(비트맵) 왼쪽, 텍스트 오른쪽
                   padx=10, pady=5)
    lbl.pack(anchor="w")

root.mainloop()
