#CSEC 472 - Authentication & Security Models
#Instructor: Chaim Sanders
#Student Name: Saad Ali Rana
#UID: 591005905
#RIT ID: sar9673@rit.edu
#Assignment: Homework 1
#Submission Date: 2/2/2016

import os
import random
import pygame, sys
from pygame.locals import *

#Position Defined
x = 200
y = 0
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

#Board and Game Definitions
CLICKS = 10
WIDTH = 600
HEIGHT = 600
BOX = 30
boxWIDTH = WIDTH / BOX
boxHEIGHT = HEIGHT / BOX

#Colors
BLACK = (0, 0, 0)
WHITE = (255,255,255)
BLUE = (0, 191, 255)
GREEN = (0, 255, 0)

#Function to Draw Board
def pullBoard():
	for x in range(0, WIDTH, BOX):
		pygame.draw.line(screen, BLUE, (x,0), (x,HEIGHT))
	for y in range(0, HEIGHT, BOX):
		pygame.draw.line(screen, BLUE, (0,y), (WIDTH, y))

#Function to Create New Instance of Drawn Board
def newBoard():
	boardBank = {}
	for y in range (boxHEIGHT):
		for x in range (boxWIDTH):
			boardBank[x,y] = 0
	return boardBank

#Function To Randomize Integer Values for Coloring Boxes
def boardAuto(golBank):
	for item in golBank:
		golBank[item] = random.randint(0,1)
	return golBank

#Function To Change Box Color Based on golBank Output
def boxColor(item, golBank):
	x = item[0]
	y = item[1]
	y = y * BOX
	x = x * BOX
	if golBank[item] == 0:
		pygame.draw.rect(screen, WHITE, (x, y, BOX, BOX))
	if golBank[item] == 1:
		pygame.draw.rect(screen, GREEN, (x, y, BOX, BOX))
	return None

#Function Checking for Live Bordering Boxes
def checkBorder(item, golBank):
	bordering = 0
	for x in range (-1,2):
		for y in range (-1,2):
			checkBox = (item[0] + x, item[1] + y)
			if checkBox[0] < boxWIDTH and checkBox[0] >= 0:
				if checkBox[1] < boxHEIGHT and checkBox[1] >= 0:
					if golBank[checkBox] == 1:
						if x == 0 and y == 0:
							bordering += 0
						else:
							bordering += 1
	return bordering

#Function To Proceed With Next Turn
def checked(golBank):
	freshCheck = {}
	for item in golBank:
		sumBordering = checkBorder(item, golBank)
		if golBank[item] == 1:
			if sumBordering < 2:
				freshCheck[item] = 0
			elif sumBordering > 3:
				freshCheck[item] = 0
			else:
				freshCheck[item] = 1
		elif golBank[item] == 0:
			if sumBordering == 3:
				freshCheck[item] = 1
			else:
				freshCheck[item] = 0
	return freshCheck

def main():
	pygame.init()
	global screen
	GAMESPEED = pygame.time.Clock()
	screen = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption('Game of Life - CSEC 472')
	screen.fill(WHITE)
	golBank = newBoard()
	golBank = boardAuto(golBank)
	for item in golBank:
		boxColor(item, golBank)
	pullBoard()
	pygame.display.update()

	#Game Initialization Loop
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		golBank = checked(golBank)

		for item in golBank:
			boxColor(item, golBank)

		pullBoard()
		pygame.display.update()
		GAMESPEED.tick(CLICKS)


if __name__=='__main__':
	main()
