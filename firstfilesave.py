import numpy as np
import matplotlib.pyplot as plt
import cv2
def drawimage(img,title="image"):
    plt.imshow(img,cmap="gray")
    plt.axis("off")
    plt.title(title+str(img.shape))
    plt.show()
img_ = cv2.imread("./Desktop/jamie_Before.jpg")
img_ = cv2.cvtColor(img_,cv2.COLOR_BGR2GRAY)
img_1 = cv2.resize(img_,(100,100))
drawimage(img_1,"james")
def convulation(img):
    w = img.shape[0]
    h = img.shape[1]
    print(w,h)
    f = 3
    blur_filter = np.array([[0.11,0.111,0.111],
                            [0.11,0.111,0.111],
                            [0.11,0.111,0.111]
                           ])
    edge_filter = np.array([[1,0,-1],
                           [1,0,-1],
                           [1,0,-1]])
    new_image = np.zeros((w-f+1,h-f+1))
    for rows in range(w-f+1):   #for the new image
        for col in range(h-f+1): #for the new image
            for i in range(f):   #for the filter
                for j in range(f):
                    new_image[rows][col] +=img[rows+i][col+j]*edge_filter[i][j]
                    if new_image[rows][col]>255:
                        new_image[rows][col] = 255
                    elif new_image[rows][col] <0:
                        new_image[rows][col]  =0
    drawimage(img)
    drawimage(new_image)
convulation(img_1)                
