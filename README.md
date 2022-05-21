# Edge-Linking-using-Hough-Transform
## Aim:
To write a Python program to detect the lines using Hough Transform.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1:
Import the required modules.

### Step2:
Import the image to operate on.

### Step3:
Convert the imported image from BGR to GRAYSCALE.

### Step4:
Find the edges using canny edge detector and display the image.

### Step5:
Detect the points that form a line using hough transform.

### Step6:
Draw the lines on the image

### Step7:
Display the output

### Step8:
End the program.
## Program:

### Read image and convert it to grayscale image
```
# Read image and convert it to grayscale image
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
```
## Output
### Input image and grayscale image
![](1.png)
### Canny Edge detector output
![](2.png)
### Display the result of Hough transform
![](3.png)
## Result:
Thus the program is written with python and OpenCV to detect lines using Hough transform. 
