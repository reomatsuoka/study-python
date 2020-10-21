# coding:utf-8
import random
import tkinter as tk
import tkinter.messagebox as tmsg


def Buttonclick():
    b = editbox1.get()


# print(str(a[0]),str(a[1]),str(a[2]),str(a[3]))
# while True:
# 4桁の数字か判別する式
    isok = False
# while isok == False:
#     b = input("数を入れてね＞")
    if len(b) != 4:
        tmsg.showerror("エラー", "４桁の数字を入れて下さい")
    else:
        kazuok = True
        for i in range(4):
            if (b[i] < "0") or (b[i] > "9"):
                tmsg.showerror("数字ではありません")
                kazuok = False
                break
        if kazuok:
            isok = True
    if isok:
        # ヒットを判定
        hit = 0
        for i in range(4):
            if a[i] == int(b[i]):
                hit = hit+1

        # ブローを判定
        blow = 0
        for j in range(4):
            for i in range(4):
                if (int(b[j]) == a[i] and (a[i] != int(b[i])) and a[j] != int(b[j])):
                    blow = blow + 1
                    break
        # ヒットが４なら当たりで終了
        if hit == 4:
            tmsg.showinfo("当たり！", "おめでとうございます。当たりです")
            root.destroy()
        else:
            rirekibox.insert(tk.END, b+"／H:"+str(hit)+" B:"+str(blow)+"\n")


a = [
    random.randint(0, 9),
    random.randint(0, 9),
    random.randint(0, 9),
    random.randint(0, 9)
]

root = tk.Tk()
root.geometry("600x400")
root.title("数当てゲーム")

rirekibox=tk.Text(root,font=("Helvetica",14))
rirekibox.place(x=400,y=0,width=200,height=400)

labell = tk.Label(root, text="数を入力してね", font=("Helvetica", 14))
labell.place(x=20, y=20)

editbox1 = tk.Entry(width=4, font=("Helvetica", 28))
editbox1.place(x=120, y=60)

button1 = tk.Button(root, text="チェック", font=(
    "Helvetica", 14), command=Buttonclick)
button1.place(x=220, y=60)

root.mainloop()
