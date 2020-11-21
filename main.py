import pygame
from math import pi
WIDTH = 800
HEIGHT = 600
FPS = 60
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Коротыч Михаил (ИУ7-25Б)")
clock = pygame.time.Clock()
def main():
	game = True
	angle = 0
	x, y = WIDTH // 2, HEIGHT // 2
	state = True
	while game:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				game = False
				return
		if x >= WIDTH - 100:
			state = False
		if x <= 0:
			state = True
		if state:
			x += 3
			angle -= pi / 24
		else:
			x -= 3
			angle += pi / 24
		screen.fill((255, 255, 255))
		ellipsis = pygame.draw.ellipse(screen, (255, 255, 255), (232, 200, 100, 100))
		pygame.draw.arc(screen, (173, 255, 47), (x, y, 100, 100), angle, pi / 2 + angle, 50)
		pygame.draw.arc(screen, (44, 123, 170), (x, y, 100, 100), pi / 2 + angle, pi + angle, 50)
		pygame.draw.arc(screen, (234, 25, 143), (x, y, 100, 100), pi + angle, 3 * pi / 2 + angle, 50)
		pygame.draw.arc(screen, (72, 10, 27), (x, y, 100, 100), 3 * pi / 2 + angle, 2 * pi + angle, 50)
		pygame.display.update()
		clock.tick(FPS)
if __name__ == '__main__':
	main()