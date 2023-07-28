import pygame, sys
from pygame.locals import *

pygame.init()

# Creacion de la ventana
window = pygame.display.set_mode((400,300))
pygame.display.set_caption("Hola como estas") # Nombre de la ventana

# Creacion de un bucle que la mantiene abierta
while True:
    for evento in pygame.event.get():
        if evento.type == QUIT: # Esto es igual a la x en las aplicaciones
            pygame.quit() # Cierra todos lo modulos
            sys.exit() # Cierra la ventana
    pygame.display.update() # Actualiza la ventana