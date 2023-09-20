import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("Pacman")
clock = pygame.time.Clock()


maze = pygame.image.load('assets/maze.png')


player = pygame.image.load('assets/player_images/1.png')
player_rect = player.get_rect(topleft = (10,325))


blueg = pygame.image.load('assets/ghost_images/blue.png')
orangeg = pygame.image.load('assets/ghost_images/orange.png')
pinkg = pygame.image.load('assets/ghost_images/pink.png')
redg = pygame.image.load('assets/ghost_images/red.png')

player_x = 10

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit
			exit()


	

	screen.blit(maze,(0,0))
	screen.blit(player,player_rect)
	screen.blit(blueg,(610,500))
	screen.blit(orangeg,(605,180))
	screen.blit(pinkg,(200,40))
	screen.blit(redg,(100,653))


	player_rect.x = player_rect.x + 1
	if player_rect.right >= 750 : player_rect.left = -5
	print(player_rect.x,player_rect.y)

	if player_rect.x == 220 : player_rect.x += 2
	if player_rect.x >= 220 : player_rect.x 
	if player_rect.x >= 220 : player_rect.y += 2
	if player_rect.y >= 390 : player_rect.y = 390
	if player_rect.y >= 390 : player_rect.x += 2
	if player_rect.x >= 420 : player_rect.x
	if player_rect.x >= 420 : player_rect.y -= 4
	if player_rect.y <= 325 : player_rect.y = 325
	if player_rect.y == 325 : player_rect.x += 2
	if player_rect.x >= 730 : player_rect.x = -10
	print(player_rect.x,player_rect.y)

	pygame.display.update()
	clock.tick(60)