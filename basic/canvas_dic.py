# coding:utf-8
import tkinter as tk
balls = [
    {"x": 400, "y": 300, "dx": +1, "dy": +1, "color": "blue"},
    {"x": 200, "y": 200, "dx": -1, "dy": +1, "color": "red"},
    {"x": 300, "y": 200, "dx": +1, "dy": -1, "color": "green"}
]


def move():
    global balls
    for b in balls:
        canvas.create_oval(b["x"] - 21, b["y"] - 21,
                           b["x"] + 21, b["y"] + 21, fill="white", width=0)
        b["x"] = b["x"] + b["dx"]
        b["y"] = b["y"] + b["dy"]
        canvas.create_oval(b["x"] - 20, b["y"] - 20, b["x"] +
                           20, b["y"] + 20, fill=b["color"], width=0)
        if b["x"] >= canvas.winfo_width():
            b["dx"] = -1
        if b["x"] <= 0:
            b["dx"] = +1
        if b["y"] >= canvas.winfo_height():
            b["dy"] = -1
        if b["y"] <= 0:
            b["dy"] = +1
    root.after(10, move)
		

root = tk.Tk()
root.geometry("600x400")

canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.place(x=0, y=0)

root.after(10, move)
root.mainloop()
