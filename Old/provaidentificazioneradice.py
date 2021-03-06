import sys
import numpy as np
import os
import cv2
from matplotlib import pyplot as plt

path = os.path.abspath(os.path.dirname(__file__)) #Salva nella variabile path il percorso globale della cartella in cui si trova il file .py in esecuzione
os.chdir(path)  # Cambio della cartella attuale nella cartella in cui si trova il file .py
img = cv2.imread('a.jpg',0)
print (img.shape)
h, w = img.shape[:2]

# Drop top and bottom area of image with black parts.
img= img[100:h-100, :]
h, w = img.shape[:2]

# Threshold image
ret,th1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY)

# get rid of thinner lines
kernel = np.ones((5,5),np.uint8)
th1 = cv2.dilate(th1,kernel,iterations = 3)

# Determine contour of all blobs found
contours0, hierarchy = cv2.findContours( th1.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours = [cv2.approxPolyDP(cnt, 3, True) for cnt in contours0]

# Draw all contours
vis = np.zeros((h, w, 3), np.uint8)
cv2.drawContours( vis, contours, -1, (128,255,255), 3, cv2.LINE_AA)

# Draw the contour with maximum perimeter (omitting the first contour which is outer boundary of image
# Not necessary in this case
vis2 = np.zeros((h, w, 3), np.uint8)
perimeter=[]
for cnt in contours[1:]:
    perimeter.append(cv2.arcLength(cnt,True))
print (perimeter)
print (max(perimeter))
maxindex= perimeter.index(max(perimeter))
print (maxindex)

cv2.drawContours( vis2, contours, maxindex +1, (255,0,0), -1)

# Show all images
titles = ['Original Image','Threshold','Contours', 'Result']
images=[img, th1, vis, vis2]
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i]), plt.xticks([]), plt.yticks([])
plt.show()

'''length = 300
(x,y),(MA,ma),angle = cv2.fitEllipse(cnt)
print(np.pi , angle)
print(angle * np.pi / 180.0)
print (np.cos(angle * np.pi / 180.0))
x2 =  int(round(x + length * np.cos((angle-90) * np.pi / 180.0)))
y2 =  int(round(y + length * np.sin((angle-90) * np.pi / 180.0)))
cv2.line(vis2, (int(x), int(y)), (x2,y2), (0,255,0),5)
print (x,y,x2,y2)'''