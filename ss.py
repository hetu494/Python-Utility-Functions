import PIL.ImageGrab
import pyautogui
import datetime

d1 = datetime.datetime.now()
d2 = d1.strftime("%Y-%M-%d %H%M%S")

print(d2)

while True:
	
	current = datetime.datetime.now()
	if (current - d1).seconds > 60:
		d2 = current.strftime("%Y-%M-%d %H%M%S")
		img = pyautogui.screenshot(str(str(d2)+'.png'))
		d1 = current