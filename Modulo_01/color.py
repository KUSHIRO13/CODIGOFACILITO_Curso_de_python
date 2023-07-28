import pygame, sys
from pygame.locals import *

pygame.init()
color = (0,140,60) # Primera forma de crear un color
color2 = pygame.Color(255,120,9) # Segunda forma de crear un color
window = pygame.display.set_mode((400,300))
pygame.display.set_caption("Color")

while True:
    window.fill(color2) # El metodo "fill" rellena la ventana de ese color
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()