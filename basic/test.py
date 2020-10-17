# coding:utf-8
print("test")
print(1+1)

#VScordでは出力されない？
#import calender
#print(calender.month(2020,10))

#\newline バックラッシュと改行文字を無視
#語尾に”\”をつける事で改行できる？
print("こんにちは。今日の晩ご飯は何でしたか？\
おいしかったですか？\
何カロリーでしたか？")

a=1
b=2
print(a+b)

for i in [1,2,3,4,5]:
  print(i)
  print("こんにちは")

for k in range(1,6+1):
  print(k)
  print("こんにちは")

for h in "Hello":
  print(h)

total = 0
a = 1
while total <= 60:
  total = total + a
  a = a + 1
print(total)

for o in range(1,15):
  if o <= 5:
    print("小さいです")
  else:
    print("大きいです")

for a in range(1,10+1):
  print(a)
  if a%2==0:
    print("○")
  if a%3==0:
    print("□")
  if a%2==0 and a%3==0:
    print("△")
  else:
    print("×")

def tashizan(a,b):
  total=0
  for i in range(a,b+1):
    total=total+i
  return total
c=tashizan(1,5)
print(c)
