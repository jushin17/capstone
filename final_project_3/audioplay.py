import pygame
import threading
import time

isThread = False

queue = []

def audioplay(filename, bitplay = 16000):
	print "AUDIO:request:%s"%filename
	global queue
	queue.append(filename)
	queue.append(bitplay)
	CheckandMake()
	

def CheckandMake():
	global isThread
	if isThread == False:
		print "[THREAD]:AUDIO:created"
		isThread = True
#		create thread by queuePlay
		th=threading.Thread(target=queuePlay)
		th.start()


def queuePlay():
	global queue
	global isThread
	while len(queue):
		filename = queue.pop(0)
		bitplay = queue.pop(0)
		pygame.mixer.init(bitplay)
		pygame.mixer.music.set_volume(10)
		pygame.mixer.music.load("sound/" + filename)
		pygame.mixer.music.play()
		while pygame.mixer.music.get_busy() == True:
			time.sleep(0.3)
			continue	
		pygame.mixer.quit()
	isThread = False
	print "[THREAD]:AUDIO:terminate"
	
	




