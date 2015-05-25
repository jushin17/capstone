import pygame

def audioplay(filename):
	pygame.mixer.init()
	pygame.mixer.music.load("audio/" + filename)
	pygame.mixer.music.play()
	
	while pygame.mixer.music.get_busy() == True:
		continue

def main():
	alphabets = ('q', 'Q', 'w', 'W', 'e', 'E', 'r', 'R', 't', 'T', 'y', 'u', 'i', 'o', 'O', 'p', 'P', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm')
	while True:
		filename = raw_input()
		if filename in alphabets:
			audioplay(filename + ".wav")
		else:
			break;

if __name__ == '__main__':
	main()
