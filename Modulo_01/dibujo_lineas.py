import pygame,sys
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((400,300))
pygame.display.set_caption("Dibujando lineas")
color1 = pygame.Color(70,80,150)
pygame.draw.line(window,color1,(60,80),(160,100),8)

while True:
    # window.fill((60,150,200))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()