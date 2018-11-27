#import-------
import pygame
from pygame.locals import *
import time
import graphics_isn as GP
from graphics_isn import Point as poo
import os

largeur=1920
hauteur=1080
#fonctions----
a,b,c=220,220,220


if __name__ == "__main__":
    GP.affiche_auto_on()
    heure = int(input("entrer le nombre d'heures du minuteur: ")) #entrer l'heure
    minute = int(input("entrer le nombre de minutes du minuteur: ")) #entrer les minutes
    seconde = int(input("entrer le nombre de secondes du minuteur: ")) #entrer les secondes
    secondetotal = (heure*3600)+(minute*60)+(seconde) #calcule les secondes au total
    timer = time.time()+secondetotal
    os.system("pause") #fonction pour windows utiliser la fonction pause du cmd pour devoir appuyer sur une touche avant que le chrono ce lance
    GP.init_graphic(largeur, hauteur, "minuteur",GP.gray,fullscreen=1) #cf moudle graphics_isn
    while timer >= time.time():
        temps = timer - time.time()
        heure= '{:02d}'.format(int(temps//60//60)) #convertion de l'heure
        minute = '{:02d}'.format(int(temps//60%60)) #convertion de minute
        seconde = round(temps % 60, 1)#convertion des secondes
        GP.aff_pol(str(heure)+":"+str(minute)+":"+str(seconde), 200, poo(410,340), GP.couleur_RGB(a,b,c), 0, 0) #affciher heure minutes secondes taille 200 point en haut a gauche a 410 340 couleur abc pas en gras pas en italique
        #time.sleep(0.125)
        GP.load_image("gears.gif",poo(0,0)) #charge et affiche l'image
        for event in pygame.event.get():
            if event.type==KEYDOWN: #si on appuie sur une touche le compteur s'arrete
                timer = 0
                pygame.quit()
        if 60*10 >= temps >= 60*5: #en dessous de dix minute deviens jaune
            a,b,c = 200,200,10
        if temps <= 60*5: #en dessous de 5 minute deviens rouge
            a,b,c = 200,10,10
    GP.draw_fill_rectangle(poo(960,540),1920,1080,GP.black) #quand on sors de la boucle affiche un rectangle noir
    GP.wait_escape("appuyer sur Echap",30)# attend d'appuyer sur echap pour quitter et affiche apuuyer sur echap

