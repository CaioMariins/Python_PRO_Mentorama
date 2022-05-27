import sys, pygame
import random
from pygame import freetype

freetype.init()
default_font = freetype.SysFont(freetype.get_default_font(), 64)

pygame.init()

size = width, height = 1240, 680
black = 0, 0, 0
white = 255,255,255
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Alien Hunt")
pygame.mouse.set_visible(0)
clock = pygame.time.Clock()


class Hunt():
    
    def __init__(self, screenheight,screenwidth,imagefile):
        self.shape = pygame.image.load(imagefile)

        self.rect = self.shape.get_rect()

        self.top = screenheight - self.shape.get_height()

        self.left = screenwidth - self.shape.get_width()

        self.score = 0

    def Show(self, surface):
        surface.blit(self.shape, (self.left,self.top))
        
    def UpdateCoords(self,x,y):
        self.left = x - self.shape.get_width()/2
        self.top = y - self.shape.get_height()/2
        self.rect.update(self.left,self.top,30,30)
        return self.left,self.top
    
    def pontuation(self):
        self.score += 1
        

class Eggs():

    def __init__(self, imagefile):
        self.shape = pygame.image.load(imagefile)
        self.rect = self.shape.get_rect()

    def generate(self,surface, largura, altura):
        self.rect.update(largura,altura,30,30)
        surface.blit(self.shape, (largura,altura))
        
def stats(score):
    default_font.render_to(screen, (4, 4), "Score:"+str(score), black, None, size=64)

hunter = Hunt(height,width,"target.png")
egg = Eggs("alien.png")
largura = random.randint(100,1140)
altura = random.randint(50,630)
val = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        pygame.Surface.fill(screen,white)
        x,y = pygame.mouse.get_pos()
        
        if val == 0:
            egg.generate(screen,largura,altura)
            if egg.rect.collidepoint(x,y) == True:
                hunter.pontuation()
                largura = random.randint(100,1140)
                altura = random.randint(50,630)
                val = 0

    hunter.UpdateCoords(x,y)
    
    hunter.Show(screen)
    
    clock.tick(60)
    stats(hunter.score)
    pygame.display.update()