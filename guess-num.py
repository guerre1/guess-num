# 題目
#  產生一個隨機整數1~100(don't print)
#  讓使用者重複輸入數字去猜
#  猜對的話 印出 "終於猜對了"
#  猜錯的話 要告訴他 比答案大/小

import random 

r = random.randint(1, 100)
while True:
	g = input('請猜數字:')
	g = int(g)
	if g == r:
		print('你猜對了')
		break
	elif g > r:
		print('答案比你猜的小')
	elif g < r:
		print('答案比你猜的大')