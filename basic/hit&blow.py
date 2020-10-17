#coding:utf-8
#ヒット＆ブロー
import random
x = random.randint(0,9)
print(x)

y = int(input("数を入力して下さい"))
if x == y:
  print("当たり")
else:
  print("はずれ")
  