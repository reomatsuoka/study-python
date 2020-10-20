#coding:utf-8
import tkinter as tk

root = tk.Tk()
root.geometry("600x400")
x=300
y=200

def click(event):
  global x,y
  canvas.create_oval(x - 21,y - 21,x + 21,y +21,fill="white",width=0)
  x=event.x
  y=event.y
  canvas.create_oval(x - 20,y - 20,x + 20,y +20,fill="red",width=0)

canvas=tk.Canvas(root,width =600 , height=400 , bg="white")
canvas.place(x=0,y=0)


canvas.bind("<Button-1>",click)
root.mainloop()