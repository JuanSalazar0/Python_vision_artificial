# Practia 2 cambio a coordenadas cromaticas
# 
# --------------------------Inicio de programa---------------------------
import numpy as np 
import cv2 
#Abrir imagen 
im= cv2.imread('Trapitos.jpg')
im2= cv2.imread('Trapitos.jpg')
height, width = im.shape[:2]
#------------------------valores para amarillo---------------------
rinf=75
rsup= 110
gsup=100
ginf=70
bsup=80
binf=59
for y in range(height):
    for x in range(width): 
        b1,g1,r1 = im2[y,x]
        h=int(int(r1)+int(b1)+int(g1))
            
        #if ((h) > 0):
        b= ((255)*b1)/h
        g= ((255)*g1)/h
        r= ((255)*r1)/h
        im2[y,x]= (b,g,r)

        if (r>rinf and r <= rsup) and (g>ginf and g <= gsup) and (b>binf and b <= bsup ):
           # im2[y,x]= (b,g,r)
           im2[y,x]= (255,255,255)
        else:
            im2[y,x]= (0,0,0)   
         
cv2.imshow('imagen',im)
cv2.imshow('imagen coordenadas',im2)
cv2.waitKey(0)
