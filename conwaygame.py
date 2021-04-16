import pygame as py
import sys
from game_window_class import *

HEIGHT,WIDTH=800,800
bg = (42,12,69)
global running
running=True
FPS=60
lol=(199,194,129)
clock=py.time.Clock()
def get_events():
    for event in py.event.get():
        if event.type == py.QUIT:
            running=False
def update():
    game.update()
def draw():
    window.fill(bg)
    game.draw()

py.init()
window=py.display.set_mode((WIDTH,HEIGHT))
game=game_window( window , 150, 300 )

while running:
    get_events()
    update()
    draw()
    py.display.update()
    clock.tick(FPS)
pygame.quit()
sys.exit()
