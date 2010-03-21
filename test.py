#!/usr/bin/env python
##
## test.py
## Login : <quentin@quentin-desktop>
## Started on  Sat Mar 20 23:52:33 2010 Quentin
## $Id$
##
## Author(s):
##  - Quentin <>
##
## Copyright (C) 2010 Quentin
##
"""
This simple example is used for the line-by-line tutorial
that comes with pygame. It is based on a 'popular' web banner.
Note there are comments here, but for the full explanation,
follow along in the tutorial.
"""


#Import Modules
import os, pygame

import data

from pygame.locals import *

# from ledossier.lefichier import lafonction
from dumbmenu.dumbmenu import dumbmenu

if not pygame.font:
    print 'Warning, fonts disabled'

if not pygame.mixer:
    print 'Warning, sound disabled'


class Snake(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer
        self.image = data.load_image('snake.png', -1)
        self.rect  = self.image.get_rect()
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.rect.move_ip(self.speed_x, self.speed_y)

    def _handle_dir_x(self, event, key, dir):
        if event.type == KEYDOWN and event.key == key:
            self.speed_x -= dir
        elif event.type == KEYUP and event.key == key:
            self.speed_x += dir

    def _handle_dir_y(self, event, key, dir):
        if event.type == KEYDOWN and event.key == key:
            self.speed_y -= dir
        elif event.type == KEYUP and event.key == key:
            self.speed_y += dir

    def handle_event(self, event):
        """ handle snake keyboard event """
        self._handle_dir_x(event, K_LEFT, 1)
        self._handle_dir_x(event, K_RIGHT, -1)
        self._handle_dir_y(event, K_UP, 1)
        self._handle_dir_y(event, K_DOWN, -1)



def main():

    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
    #Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((480, 360))
    pygame.display.set_caption('Monkey Fever')
    pygame.mouse.set_visible(0)

    red   = 255,  0,  0
    green = 0,  255,  0
    blue  = 0,    0,255
    result = dumbmenu(screen, [
                               'Start Game',
                               'Options',
                               'Manual',
                               'Show Highscore',
                               'Quit Game'], 64,64,32,1.4, green,blue,red)
    print "Result: ", result
    if result == 4:
        exit()
    #Create The Backgound
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    #Put Text On The Background, Centered
#     if pygame.font:
#         font = pygame.font.Font(None, 36)
#         text = font.render("Pummel The Chimp, And Win $$$", 1, (10, 10, 10))
#         textpos = text.get_rect(centerx=background.get_width()/2)
#         background.blit(text, textpos)

    #Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()

    snake = Snake()

    #Prepare Game Objects
    clock = pygame.time.Clock()
    allsprites = pygame.sprite.RenderPlain((snake))

    #Main Loop
    while 1:
        clock.tick(60)

        #Handle Input Events
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                print "Received event:", event

            if event.type == KEYDOWN or event.type == KEYUP:
                snake.handle_event(event)

            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == MOUSEBUTTONDOWN:
                pass
            elif event.type is MOUSEBUTTONUP:
                pass

        allsprites.update()

        #Draw Everything
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()

#Game Over


#this calls the 'main' function when this script is executed
if __name__ == '__main__':
    main()
