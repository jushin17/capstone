import pygame

def audioplay(filename):
	pygame.mixer.init()
	pygame.mixer.music.load("audio/" + filename)
	pygame.mixer.music.play()
	
	while pygame.mixer.music.get_busy() == True:
		continue

def main():
	audioplay("audio.wav")

if __name__ == '__main__':
	main()
