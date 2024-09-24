import pygame, sys
from numpy import random
import numpy as np


class Game:
    def __init__(self):
        self.SCREEN_WIDTH = 500
        self.SCREEN_HEIGHT = 400
        self.TILE_SIZE = 20

        self.running = False

        pygame.display.set_caption("Conway's Game of Life")
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        
        self.clock = pygame.time.Clock()

        '''
        HOLY SHIT PYTHON ARRAYS ARE SO FUCKING BADDDDDDDDD
        DEADASS
        EVERY PROBLEM I HAD
        WAS WITH FUCKING ARRAYYYYSSS
        '''

        self.array1 = np.array([[0 for i in range(int(self.SCREEN_WIDTH/self.TILE_SIZE))] for j in range(int(self.SCREEN_HEIGHT/self.TILE_SIZE))])
        self.array2 = np.array([[0 for i in range(int(self.SCREEN_WIDTH/self.TILE_SIZE))] for j in range(int(self.SCREEN_HEIGHT/self.TILE_SIZE))])
    
    def runSimulation(self):
        while True:
            self.screen.fill((0, 0, 0))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousex,mousey = pygame.mouse.get_pos()
                    x = int(mousex/self.TILE_SIZE)
                    y = int(mousey/self.TILE_SIZE)
                    if self.array1[y][x] == 1:
                        self.array1[y][x] = 0
                    else:
                        self.array1[y][x] = 1
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.running = True if not self.running else False
                    elif event.key == pygame.K_RETURN:
                        for y in range (len(self.array1)):
                            for x in range (len(self.array1[y])):
                                self.array1[y][x] = random.randint(2)
                    elif event.key == pygame.K_r:
                        self.array1 = np.array([[0 for i in range(int(self.SCREEN_WIDTH/self.TILE_SIZE))] for j in range(int(self.SCREEN_HEIGHT/self.TILE_SIZE))])

            self.drawSquares(self.array1)

            if self.running:
                self.array2 = self.array1.copy()
                for y in range(len(self.array2)):
                    for x in range(len(self.array2[y])):
                        n = self.countNeighbors(self.array1, x, y)
                        if self.array1[y][x] == 1 and (n > 3 or n < 2):
                            self.array2[y][x] = 0
                        elif self.array1[y][x] == 0 and n == 3:
                            self.array2[y][x] = 1
                        else:
                            self.array2[y][x] = self.array1[y][x]
                
                self.array1 = self.array2.copy()

            pygame.display.update()
            self.clock.tick(12)
    
    
    
    def drawSquares(self, array):
        for y in range(len(array)):
            for x in range(len(array[y])):
                color = (255*array[y][x],255*array[y][x],255*array[y][x])
                pygame.draw.rect(self.screen, color, pygame.Rect(x*self.TILE_SIZE+2, y*self.TILE_SIZE+2,self.TILE_SIZE-2, self.TILE_SIZE-2))
    
    def swapArray(self):
        temp = self.curr_array
        self.curr_array = self.hidden_array
        self.hidden_array = temp
    def countNeighbors(self, array, x, y):
        sum = 0
        
        #search 3x3
        for i in range(-1,2): #-1 kay mo back og one, and 2 kay exclusive
            for j in range(-1, 2):
                '''
                balihon siya kay idk what the fawk is happening.
                if coord+i or coord+j is out of range
                Set i or j into n-1 (size of array)
                it is set to either negative or positive depending on which direction
                up, left(negative)
                down, right(positive)
                '''
                if y+i > len(array)-1:
                    i = -len(array)+1
                elif y+i < 0:
                    i = len(array)-1
                if x+j > len(array[y])-1:
                    j= -len(array[y])+1
                elif x+j < 0:
                    j = len(array[y])-1
                
                sum += array[y+i][x+j]
        
        return sum - array[y][x]
        

            
game = Game()
game.runSimulation()