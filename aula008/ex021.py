import pygame
pygame.init()
pygame.mixer.music.load(
    'megalovania.mp3')
pygame.mixer.music.play()
pygame.event.wait()
