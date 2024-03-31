import random
a = input('請輸入範圍最小值: ')
b = input('請輸入範圍最大值: ')
a = int(a)
b = int(b)

r = random.randint(a, b)
count = 0
while True:
	count += 1 # count = count + 1
	g = input('請輸入您要猜的數字: ')
	g = int(g)
	if g == r:
		print('終於猜對了!')
		print('這是您猜的第', count, '次')
		break
	elif g > r:
		print('您猜的數字太大')
	elif g < r:
		print('您猜的數字太小')
	print('這是您猜的第', count, '次')