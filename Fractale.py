# Créé par Eleve, le 28/11/2022 en Python 3.7


import pygame



MAX_ITERATION = 200 #prend trop de temps si il y a trop de calcul
XMIN, XMAX, YMIN, YMAX = -2, +0.5, -1.25, +1.25
LARGEUR, HAUTEUR = 1020, 1020

pygame.init()
surface = LARGEUR, HAUTEUR





screen = pygame.display.set_mode((LARGEUR, HAUTEUR), pygame.RESIZABLE)
pygame.display.set_caption("Mandelbrot Set")




for y in range(HAUTEUR):
  for x in range(LARGEUR):

    cx = (x * (XMAX - XMIN) / LARGEUR + XMIN)
    cy = (y * (YMIN - YMAX) / HAUTEUR + YMAX)
    xn = 0
    yn = 0
    n = 0
    while (xn * xn + yn * yn) < 4 and n < MAX_ITERATION:
      tmp_x = xn
      tmp_y = yn
      xn = tmp_x * tmp_x - tmp_y * tmp_y + cx
      yn = 2 * tmp_x * tmp_y + cy
      n = n + 1
    if n == MAX_ITERATION:
      screen.set_at((x, y), (191,62,255))
    else:
      screen.set_at((x, y), (169,169,169))
pygame.display.flip()


loop = True
while loop:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      loop = False


pygame.quit()

#191,62,255
#169,169,169