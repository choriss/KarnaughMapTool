import tkinter as tk

# データを設定
data = [
    ["A1", "B1", "C1"],
    ["A2", "B2", "C2"],
    ["A3", "B3", "C3"]
]

# ホバー時の色を変える関数
def on_enter(event, label):
    label.config(bg="lightblue")

# ホバーから離れた時の色を戻す関数
def on_leave(event, label):
    label.config(bg="white")

# ラベルに表示するテキストをクリックした時の動作
def on_click(event, text):
    print(f"Clicked on: {text}")

# Tkinterウィンドウの設定
root = tk.Tk()
root.title("2次元配列をラベルで表示")

for i, row in enumerate(data):
    for j, cell in enumerate(row):
        label = tk.Label(root, text=cell, bg="white", borderwidth=1, relief="solid", width=10, height=3)
        label.grid(row=i, column=j, padx=1, pady=1)
        
        # マウスがラベルに入った時のイベント
        label.bind("<Enter>", lambda event, lbl=label: on_enter(event, lbl))
        # マウスがラベルから離れた時のイベント
        label.bind("<Leave>", lambda event, lbl=label: on_leave(event, lbl))
        # ラベルがクリックされた時のイベント
        label.bind("<Button-1>", lambda event, text=cell: on_click(event, text))

root.mainloop()
