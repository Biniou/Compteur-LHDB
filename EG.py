largeur=1920
hauteur=1080
#import-------
import pygame
from pygame.locals import *
import time
import graphics_isn as GP
from graphics_isn import Point as poo
import os
#fonctions----



if __name__ == "__main__":
    GP.change_font("Consolas")
    GP.affiche_auto_on()
    heure = int(input("entrer le nombre d'heures du minuteur: "))
    minute = int(input("entrer le nombre de minutes du minuteur: "))
    seconde = int(input("entrer le nombre de secondes du minuteur: "))
    secondetotal = (heure*3600)+(minute*60)+(seconde)
    timer = time.time()+secondetotal
    os.system("pause")
    GP.init_graphic(largeur, hauteur, "minuteur", bg_color=GP.blue, fullscreen=1)
    while timer >= time.time():
        temps = timer - time.time()
        heure= '{:02d}'.format(int(temps//60//60))
        minute = '{:02d}'.format(int(temps//60%60))
        seconde = round(temps % 60, 1)
        GP.draw_fill_rectangle(poo(largeur // 8 + largeur // 8 // 2, hauteur // 10 + hauteur // 10 // 2),1920, 100,GP.blue)
        time.sleep(0.1)
        GP.aff_pol(str(heure), 35, poo(largeur//10,hauteur//10), GP.green, 0, 1)
        GP.aff_pol(str(minute), 35, poo(largeur // 8, hauteur // 10), GP.green, 0, 1)
        GP.aff_pol(str(seconde), 35, poo(largeur // 6, hauteur // 10), GP.green, 0, 1)
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                timer = 0
                pygame.quit()


