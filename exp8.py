# Read image and convert it to grayscale image
import cv2
import numpy as np
import matplotlib.pyplot as plt
BGR_image=cv2.imread('road.jpg')
gray=cv2.cvtColor(BGR_image,cv2.COLOR_BGR2GRAY)
plt.imshow(BGR_image,"original_image")
plt.imshow(gray,"GRAY_SCALE IMAGE")
img= cv2.GaussianBlur(BGR_image,(3,3),0)
plt.imshow(img)
# Find the edges in the image using canny detector and display
edges1 = cv2.Canny(img,100,200)
plt.imshow(edges1,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
# Detect points that form a line using HoughLinesP
lines=cv2.HoughLinesP(edges1,1,np.pi/180, threshold=80, minLineLength=50,maxLineGap=250)
# Draw lines on the image
for line in lines:
    x1, y1, x2, y2 = line [0] 
    cv2.line(BGR_image,(x1, y1),(x2, y2),(210,100,200),3)
# Display the result
plt.imshow(BGR_image)