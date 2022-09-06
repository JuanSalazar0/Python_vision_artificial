import cv2 as cv
import numpy as np

img = cv.imread("vivi.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_gaussian = cv.GaussianBlur(gray,(5,5),0)

#Prewitt
kernelx = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
kernely = np.array([[1,1,1],[0,0,0],[-1,-1,-1]]) 
img_prewittx = cv.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv.filter2D(img_gaussian, -1, kernely)

#Sobel
img_sobelx = cv.Sobel(img_gaussian,cv.CV_8U,1,0,ksize=3)
img_sobely = cv.Sobel(img_gaussian,cv.CV_8U,0,1,ksize=3)
img_sobel = img_sobelx + img_sobely

#Laplaciano
img_lapl = cv.Laplacian(img_gaussian,cv.CV_8U,ksize=3)

#Impresion
prew = cv.hconcat([img_prewittx, img_prewitty])
cv.imshow("Original Image", img)
cv.imshow("prex prey", prew)
cv.imshow("Sobel", img_sobel)
cv.imshow("Laplaciano", img_lapl)

cv.waitKey(0)
cv.destroyAllWindows()