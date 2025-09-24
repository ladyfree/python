#! python3
import tkinter as tk
from tkinter import ttk
import pyautogui
from pynput import mouse

class MouseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("마우스 좌표 트래커 (Tkinter + Listbox)")
        self.root.geometry("420x420")
        self.listener = None

        # 좌표 라벨(실시간)
        self.pos_label = ttk.Label(root, text="X: ----  Y: ----", font=("맑은 고딕", 14))
        self.pos_label.pack(pady=10)

        # 버튼 영역
        btn_frame = ttk.Frame(root)
        btn_frame.pack(pady=5)

        self.start_btn = ttk.Button(btn_frame, text="시작", command=self.start_listen)
        self.start_btn.grid(row=0, column=0, padx=4)

        self.stop_btn = ttk.Button(btn_frame, text="중지", command=self.stop_listen, state=tk.DISABLED)
        self.stop_btn.grid(row=0, column=1, padx=4)

        self.clear_btn = ttk.Button(btn_frame, text="지우기", command=self.clear_listbox)
        self.clear_btn.grid(row=0, column=2, padx=4)

        # Listbox + Scrollbar
        list_frame = ttk.Frame(root)
        list_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.listbox = tk.Listbox(list_frame, font=("Consolas", 12))
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        # 좌표 실시간 업데이트 루프
        self.update_position_loop()

        # 창 닫을 때 정리
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def update_position_loop(self):
        """pyautogui로 현재 마우스 좌표를 주기적으로 읽어 라벨에 표시"""
        try:
            x, y = pyautogui.position()
            self.pos_label.config(text=f"X: {str(x).rjust(4)}  Y: {str(y).rjust(4)}")
        except Exception:
            # 드물게 포커스 이슈 등으로 실패할 수 있어 조용히 무시
            pass
        # 80ms마다 갱신
        self.root.after(80, self.update_position_loop)

    # ---- 글로벌 클릭 리스너 제어 ----
    def start_listen(self):
        if self.listener is None:
            self.listener = mouse.Listener(on_click=self.on_click)
            self.listener.start()
            self.start_btn.config(state=tk.DISABLED)
            self.stop_btn.config(state=tk.NORMAL)

    def stop_listen(self):
        if self.listener is not None:
            self.listener.stop()
            self.listener = None
            self.start_btn.config(state=tk.NORMAL)
            self.stop_btn.config(state=tk.DISABLED)

    def on_click(self, x, y, button, pressed):
        """pynput 콜백(백그라운드 스레드). 왼쪽 버튼 눌렀을 때 Listbox에 추가."""
        # Tk 위젯은 메인 스레드에서만 건드려야 하므로 after로 래핑
        if pressed and getattr(button, "name", "") == "left":
            self.root.after(0, lambda: self.listbox.insert(tk.END, f"CLICK  X,Y: {x:4},{y:4}"))

    # ---- 기타 ---
    def clear_listbox(self):
        self.listbox.delete(0, tk.END)

    def on_close(self):
        self.stop_listen()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    # ttk 기본 스타일 약간 개선(선택)
    try:
        from tkinter import ttk
        style = ttk.Style()
        if "clam" in style.theme_names():
            style.theme_use("clam")
    except Exception:
        pass

    app = MouseTrackerApp(root)
    root.mainloop()
