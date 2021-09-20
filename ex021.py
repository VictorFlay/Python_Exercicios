import pygame
print('\nEstá escutando? Isso é hardcore!\n')
print('Artista: Satanic Surfers \nMúsica: Better off Today')
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

