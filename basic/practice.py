#coding:utf-8
#ヒット＆ブロー
import random
a = random.randint(0,9)
print(a)

b = int(input("数を入力して下さい>>"))
if a == b:
  print("当たり")
else:
  print("はずれ")

import random
a=[random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)]
print(str(a[0]),str(a[1]),str(a[2]),str(a[3]))

import random

#4桁の数字か判別する式
isok = False
while isok == False:
  b=input("数を入れてね＞")
  if len(b) !=4:
    print("４桁の数字を入れて下さい")
else:
  # if(b[0]<"0") or (b[0]>"9"):
  #   print("数字ではありません")
  # elif(b[1]<"0") or (b[1]>"9"):
  #   print("数字ではありません")
  # elif(b[2]<"0") or (b[2]>"9"):
  #   print("数字ではありません")
  # elif(b[3]<"0") or (b[3]>"9"):
  #   print("数字ではありません")
  # else:
#上の式を書き直す

  #各桁が数字かどうかの判別する式
  kazuok = True
for i in range(4):
  if(b[i]<"0") or (b[i]>"9"):
    print("数字ではありません")
    kazuok = False
    break
if kazuok:
    isok=True

#ヒットを判定
hit=0
for i in range(4):
  if a[i]==int(b[i]):
    hit=hit+1

#ブローを判定
blow = 0
for j in range(4):
  for i in range(4):
    if (int(b[j])==a[i]) :
      blow = blow + 1
      break