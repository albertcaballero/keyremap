import keyboard as kb
import time

while 1:
	if kb.is_pressed ('end'):
		kb.send ('esc')
	if kb.is_pressed ('page up'):
		kb.send ('volume up')
	if kb.is_pressed('page down'):
		kb.send ('volume down')
	if kb.is_pressed ('q+u+i+t'):
		break
	time.sleep(0.1)