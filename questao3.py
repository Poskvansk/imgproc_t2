import cv2
import numpy as np
from matplotlib import pyplot as plt


def show(img):

    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def binarization(img):

    # binary_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # binary_img = cv2.equalizeHist(img)

    ret,binary_img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

    return binary_img

def fill_holes(img):
    
    negative = cv2.bitwise_not(img)

    aux = negative.copy()

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))

    negative = cv2.morphologyEx(negative, cv2.MORPH_OPEN, kernel)

    cv2.floodFill(aux, None, (5,5), 255)

    aux = cv2.bitwise_not(aux)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))

    filled = cv2.bitwise_or(negative, aux)
    filled = cv2.morphologyEx(filled, cv2.MORPH_CLOSE, kernel)

    return filled

def watershed(img):

    kernel = np.ones((3,3),np.uint8)

    sure_bg = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernel, iterations=2)
    # show(sure_bg)

    dist_transform = cv2.distanceTransform(img, cv2.DIST_L2, 3)
    # show(dist_transform)

    ret, sure_fg = cv2.threshold(dist_transform,0.3*dist_transform.max(),255,0)
    sure_fg = np.uint8(sure_fg)

    unknown = cv2.subtract(sure_bg, sure_fg)

    # # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)

    # # Add one to all labels so that sure background is not 0, but 1
    markers = markers + 1

    # # Now, mark the region of unknown with zero
    markers[unknown==255] = 0

    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    markers = cv2.watershed(img, markers)
    img[markers == -1] = [255,0,0]  

    return img

def main():

    img = cv2.imread("imagens/img_cells.jpg",0)

    binary_img = binarization(img)

    filled = fill_holes(binary_img)

    test = watershed(filled)
    show(test)
    # test[] = (0,0,255)
    show(test)

    test2 = cv2.bitwise_not(test)
    show(test2)

main()