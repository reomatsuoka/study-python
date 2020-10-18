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

import random
a=[random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)]
print(str(a[0]),str(a[1]),str(a[2]),str(a[3]))

import random

isok = False
while isok == False:
  b=input("数を入れてね＞")
  if len(b) !=4:
    print("４桁の数字を入れて下さい")
else:
  isok=True

print(b[0])
print(b[1])
print(b[2])
print(b[3])

