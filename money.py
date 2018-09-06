import os
import time

def tap_screen(x, y):
	os.system('adb -s 1a4db670ec0b7ece shell input tap {} {}'.format(x,y))
def do_money_work():
	print('#0 start game')
	# click the chuang guan button
	tap_screen(2170, 1200)
	print('#click chuangguan')

	for i in range(1000):
		time.sleep(15)
		print('after sleep for loading')
                for m in range(5):
			tap_screen(1170, 600)
			time.sleep(0.1)

		print('after clicking the starting screens')
		time.sleep(90)

		print('#wait middle')

		for j in range(20):
			tap_screen(1170, 600)
			time.sleep(0.1)

		time.sleep(24)

		print('#wait after done')

		for k in range(20):
			tap_screen(1170, 600)
			time.sleep(0.1)

		# click the end screen
		tap_screen(1520, 1050)
		print('#click end screen')
		time.sleep(5)
		# click the try again button
		tap_screen(2510, 1295)
		print('#click try again button')
		time.sleep(3)

		# click the chuang guan button
		tap_screen(2170, 1200)
		print('#click chuangguan')
		print('round #{}'.format(i+1))

if __name__=='__main__':

		do_money_work()
