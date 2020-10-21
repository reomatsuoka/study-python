# coding:utf-8
import tkinter as tk
class Ball:
    def _init_(self, x, y, dx, dy, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color

def move(self,canvas):
        canvas.create_oval(self.x - 21, self.y - 21,self.x + 21, self.y + 21,fill="white", width=0)
        self.x = self.x + self.dx
        self.y = self.y + self.dy 
        canvas.create_oval(self.x - 20, self.y - 20, self.x +20, self.y + 20, fill=b["color"], width=0)
        if self.x >= canvas.winfo_width():
            self.dx = -1
        if self.x <= 0:
            self.dx = +1
        if self.y >= canvas.winfo_height():
            self.dy = -1
        if self.y <= 0:
            self.dy = +1
    root.after(10, move)
		

root = tk.Tk()
root.geometry("600x400")

canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.place(x=0, y=0)

root.after(10, move)
root.mainloop()

def test(self)
	print(self.x)
	print(self.y)


balls = [
    {"x": 400, "y": 300, "dx": +1, "dy": +1, "color": "blue"},
    {"x": 200, "y": 200, "dx": -1, "dy": +1, "color": "red"},
    {"x": 300, "y": 200, "dx": +1, "dy": -1, "color": "green"}
]


