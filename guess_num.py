import random

r = random.randint(1, 100)
while True:
	g = input('請輸入您要猜的數字: ')
	g = int(g)
	if g == r:
		print('終於猜對了!')
		break
	elif g > r:
		print('您猜的數字太大')
	elif g < r:
		print('您猜的數字太小')