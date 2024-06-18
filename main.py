import tkinter 

root = tkinter.Tk()
root.geometry("800x600")

karnaugh_canvas = tkinter.Canvas(root, width = 400, height = 600)
karnaugh_canvas.grid(row=0,column=0)

truth_table_canvas = tkinter.Canvas(root, width = 400, height = 600)
truth_table_canvas.grid(row=0,column=1)


# truthtable

def on_truth_click(event,id,label):
    # print(f"Clicked on: {id}")
    label.config(text="0" if label.cget("text")=="1" else "1")
    truth_table_arr[id] = 0 if truth_table_arr[id]==1 else 1

truth_table_arr = [0]*16

# 配列に沿って真理値表を作成
header_label = [None]*5
abcd="abcdF"
for i in range(5):
    header_label[i] = tkinter.Entry(truth_table_canvas,width=4)
    header_label[i].grid(row=0, column=i)
    header_label[i].insert(0, abcd[i])


for i in range(16):
    i_bin = bin(i)[2:].zfill(4)
    for j in range(4):
        label = tkinter.Label(truth_table_canvas, text=i_bin[j], borderwidth=1,  relief="solid", width=2, height=2)
        label.grid(row=i+1, column=j, sticky="nsew")
    label = tkinter.Label(truth_table_canvas, text=truth_table_arr[i], borderwidth=2, relief="solid" , width=2, height=2)
    label.grid(row=i+1, column=4, sticky="nsew")

    label.bind("<Button-1>", lambda event, id=i,lbl=label: on_truth_click(event, id,lbl))


#カルノーマップ


root.mainloop()