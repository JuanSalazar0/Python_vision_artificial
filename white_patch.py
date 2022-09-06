 # Practia 2 cambio a coordenadas cromaticas
# 
# --------------------------Inicio de programa---------------------------
import numpy as np 
import cv2 
#Abrir imagen 
im= cv2.imread('Trapitos.jpg')
im2= cv2.imread('Trapitos.jpg')
height, width = im.shape[:2]



#------------------------rosa---------------------
rinf=190
rsup= 255
gsup=255
ginf=75
bsup=255
binf=0
#------------------amarillo para trapo------------------
#rinf=130
#rsup= 160
#gsup=140
#ginf=100
#bsup=100
#binf=50

#rinf=143
#rsup= 255
#gsup=222
#ginf=108
#bsup=96
#binf=0

#rinf=100
#rsup= 117.5
#gsup=66
#ginf=60
#bsup=38.5
#binf=0

maxr=0
maxg=0
maxb=0
#For para la deteccion de valores maximos
for y in range(height):
    for x in range(width): 
            b2,g2,r2 = im2[y,x]
            if r2>maxr:
                maxr=r2
            if g2>maxg:
                maxg=g2
            if b2>maxb:
                maxb=b2

maxr=np.amax(r2)
maxb=np.amax(b2)
maxg=np.amax(g2)

cr=float(255)/maxr
cg=float(255)/maxg
cb=float(255)/maxb

print("Rmax=",maxr,"cr=",cr)
print("Gmax=",maxg,"cg=",cg)
print("Bmax=",maxb,"cb=",cb)

for y in range(height):
    for x in range(width): 
        b1,g1,r1 = im2[y,x]
        
        r= cr*r1
        g= cg*g1
        b= cb*b1

        if (r>rinf*cr and r <= rsup*cr) and (g>ginf*cg and g <= gsup*cg) and (b>binf*cb and b <= bsup*cb ):
            #im2[y,x]= (b,g,r)
            im2[y,x]= (255,255,255)
        else:
            im2[y,x]= (0,0,0)   
         
cv2.imshow('imagen',im)
cv2.imshow('imagen whitepatch',im2)
cv2.waitKey(0)