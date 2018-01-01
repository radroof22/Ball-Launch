import sys, pygame
from pygame.locals import *
import random

x = 740
y = 34
y1 = 20

pygame.init()

black = (0, 0, 0)
white = (255,255,255)
red = (255,0,0)
green = (0,200,0)
blue = (0,0,200)
bright_blue = (0,0,255)
bright_green = (0,255,0)

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Ball Launch')

enemy = pygame.image.load('billCypher.png')

clock = pygame.time.Clock()

def button(msg, x, y, w, h, a, i, action = None):
	mouse = pygame.mouse.get_pos()
	
	click = pygame.mouse.get_pressed()
	
	
	if x + w > mouse[0] > x and y + h > mouse[1] > y:
		pygame.draw.rect(gameDisplay, a, (x, y, w, h))
		if click[0] == 1 and action != None:
			action()
			
	
	else:
	
		pygame.draw.rect(gameDisplay, i, (x, y, w, h))

	
	smallText = pygame.font.SysFont('comicsansms', 20)
	textSurf, textRect = text_objects(msg, smallText)
	textRect.center = ( x+(w/2), (y + (h/2)) )
	gameDisplay.blit(textSurf, textRect)
	
def quit_one():
	pygame.quit()
	quit()
	
def game_intro():
	
	intro = True
	
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
		gameDisplay.fill(black)
		largeText = pygame.font.SysFont("comicsansms", 100)
		TextSurf, TextRect = text_objects('Ball Launch', largeText)
		TextRect.center = ((display_width / 2),(display_height / 2) )
		gameDisplay.blit(TextSurf, TextRect)
		
		button('GO!',150, 450, 100, 50, green, bright_green, game_loop)
		
		button('Quit',550, 450, 100, 50, blue, bright_blue, quit_one)
		
		
		pygame.display.update()
		clock.tick(15)

def unpause():
	global pause
	pause = False
	
	pygame.mixer.music.unpause()


		
def paused():
	
	pygame.mixer.music.pause()
	
	largeText = pygame.font.SysFont("comicsansms", 115)
	TextSurf, TextRect = text_objects('Paused', largeText)
	TextRect.center = ((display_width / 2),(display_height / 2) )
	gameDisplay.blit(TextSurf, TextRect)
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		
		button('Continue',150, 450, 100, 50, green, bright_green, unpause)
		
		button('Quit',550, 450, 100, 50, blue, bright_blue, quit_one)
		
		
		pygame.display.update()
		clock.tick(15)
		

def text_objects(text, font):
	textSurface = font.render(text, True, red)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.SysFont("comicsansms", 115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width / 2),(display_height / 2) )
	gameDisplay.blit(TextSurf, TextRect)                                           
	
	pygame.display.update()
	
	time.sleep(2)
	
	game_loop()
	
def bill(count):
	global y1

	if count % 20 == 0 and count > 20:
		y1 = random.randint(20,580)

	global y 
	y = y1
	x = 740
		
		

	gameDisplay.blit(enemy, (x,y1))


def things_hit(count):
	count = int(count / 9)
	font = pygame.font.SysFont(None, 25)
	text = font.render("Score: " + str(count), True, bright_green)
	gameDisplay.blit(text, (0,0))
	
def route(x,y):
	
	if x < 0 or y < 0:
		x,y = 0,600
		
	return (x,y)

def parabola(x,y,diff):
	
	add = random.randint(5,10)
	
	if x > (800-diff):
		y += add
	else:
		y -= add
	x += 10
	
	return (x,y)
	
	
def game_loop():
	
	global y1
	global pause
		
	#pygame.mixer.music.play(-1)
	
	tup = (-23,611)
	
	count = 5
	
	thing_width = 61
	thing_height = 104
	
	
	ball_x = 740
	
	place= (0,600)
	gameExit = False
	x_diff = 100
	count1 = 0
	while gameExit == False:
		
		
		gameDisplay.fill(black)
		
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if click[0] == 1:
				x_int = mouse[0]
				x_diff = (800 - x_int) / 2
				y_int = mouse[1]
				tup = route(x_int,y_int)
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					pause = True
					paused()
		count +=1
		
		bill(count)
		
		x_int = tup[0] 
		y_int = tup[1] 
		tup = parabola(x_int,y_int,x_diff)


		things_hit(count1)
		pygame.draw.circle(gameDisplay, white, tup, 30)
		
		if tup[1] < y1 + thing_height:
			
			if tup[0] > ball_x and tup[0] < ball_x + thing_width or tup[0] + 30 > ball_x and tup[0] + 30 < ball_x +thing_width:
				
				count1 += 1
			
		pygame.display.update()
		clock.tick(60)

game_intro()

pygame.quit()
quit()

