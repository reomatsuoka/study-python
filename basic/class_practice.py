# coding:utf-8
class TestClass:
	def __init__(self, code,name):
		self.code = code
		self.name = name
classes=[]
classes.append(TestClass(1,"テスト１"))
for b in classes:
	print(str(b.code))
	print(b.name)
