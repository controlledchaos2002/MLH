import pygame as py
vec=py.math.Vector2





class game_window:
    def __init__(self , screen , x , y):
        self.screen=screen
        self.pos = vec(x,y)
        self.width,self.height=500,500
        self.image=py.Surface((self.width,self.height))
        self.rect=self.image.get_rect()
        self.rows=10
        self.columns=10
        self.grid=[]
    def update(self):
        self.rect.topleft=self.pos
    def draw(self):
        self.image.fill((102,102,102))
        self.screen.blit( self.image , (self.pos.x,self.pos.y) )
