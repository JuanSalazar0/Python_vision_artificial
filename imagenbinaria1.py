#Algoritmos para un sistema de deteccion de objetos 
#Descriptor simple 
#region de pixels conectados
# libreria python que genera puntos aleatorios y da el color RGB
# for que recorra la imagen para evaluar los valores RGB y
# generar una imagen binaria 
# Usar coordenas cromaticas para evitar modificaciones, color invariante 
# R+G+B=1 
# algoritmo White-patch
# Practica 1 inicial 
# Practia 2 cambio a coordenadas cromaticas
# Practica 3 algoritmo white patch 
# 
# --------------------------Inicio de programa---------------------------
import numpy as np 
import cv2 
#Abrir imagen 
im= cv2.imread('Trapitos.jpg')
im2= cv2.imread('Trapitos.jpg')
height, width = im.shape[:2]
#tamaño de imagen altura 731* ancho 735
#RGB de amarillo emoji = rgb(255,222,52)
#rinf=182
#rsup= 255
#gsup=222
#ginf=115
#bsup=52
#binf=0

#---------------int 1 re foto
#rinf=143
#rsup= 255
#gsup=222
#ginf=108
#bsup=96
#binf=0

#-----------------------amarillo opaco--------------
#141,111,67
#168,137,81

rinf=130
rsup= 160
gsup=140
ginf=100
bsup=100
binf=50


#------------------------rosa---------------------
#rinf=190
#rsup= 255
#gsup=255
#ginf=75
#bsup=255
#binf=0

for y in range(height):
    for x in range(width): 
        b,g,r = im2[y,x]
        if (r>rinf and r <= rsup) and (g>ginf and g <= gsup) and (b>binf and b <= bsup ):
        #if (r == 243) & (g == 247) & ( b == 7 ):
            #im2[y,x]= (0,0,0)
            im2[y,x]= (255,255,255)
            #im2[y,x]= (b,g,r)
        else:
         im2[y,x]= (0,0,0)   
         #im2[y,x]= (255,255,255)

cv2.imshow('imagen',im)
cv2.imshow('imagen bi',im2)
cv2.waitKey(0)





