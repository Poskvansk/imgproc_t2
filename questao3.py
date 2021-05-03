import cv2
import numpy as np
from matplotlib import pyplot as plt


def show(img):

    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def binarization(img):

    binary_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    binary_img = cv2.equalizeHist(binary_img)

    ret,binary_img = cv2.threshold(binary_img, 120, 255, cv2.THRESH_BINARY)

    return binary_img

def bwareaopen(img):

    return

def fill_holes(img):
    
    negative = cv2.bitwise_not(img)

    aux = negative.copy()
    # show(negative)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))

    negative = cv2.morphologyEx(negative, cv2.MORPH_ERODE, kernel)

    cv2.floodFill(aux, None, (5,5), 255)

    aux = cv2.bitwise_not(aux)

    show(negative)
    show(aux)

    test = negative | aux
    test = cv2.morphologyEx(test, cv2.MORPH_CLOSE, kernel)

    show(test)

    return

def watershed(img):


    # ret, markers = cv2.connectedComponents(img)


    # markers = cv2.watershed(img, markers)
    # watershed[markers == -1] = [255,0,0]
    # show(watershed)

    # img = cv2.imread('coins.png')
    # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    # show(thresh)

    #     # noise removal
    # kernel = np.ones((3,3),np.uint8)
    # close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
    # show(close)
    # opening = cv2.morphologyEx(close,cv2.MORPH_OPEN,kernel, iterations = 2)
    # show(opening)
    # erosion = cv2.morphologyEx(opening, cv2.MORPH_ERODE, kernel, iterations=2)
    # show(erosion)
    # # sure background area
    # sure_bg = cv2.dilate(opening,kernel,iterations=1)
    # show(sure_bg)
    # # Finding sure foreground area
    # dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
    # ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
    # # Finding unknown region
    # sure_fg = np.uint8(sure_fg)
    # unknown = cv2.subtract(sure_bg,sure_fg)

    # show(sure_fg)
    # show(unknown)

    # # Marker labelling
    # ret, markers = cv2.connectedComponents(sure_fg)
    # # Add one to all labels so that sure background is not 0, but 1
    # markers = markers+1
    # # Now, mark the region of unknown with zero
    # markers[unknown==255] = 0


    # markers = cv2.watershed(img,markers)
    # img[markers == -1] = [255,0,0]  

    # show(img)

    return


def get_areas(img):

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

    img = cv2.bitwise_not(img)

    background = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernel,iterations=2)

    # show(background)

    dist_transform = cv2.distanceTransform(img, cv2.DIST_L2, 3)
    
    ret, sure_fg = cv2.threshold(dist_transform, 0.2*dist_transform.max(),255,0)

    show(dist_transform)

    sure_fg = np.uint8(sure_fg)
    show(sure_fg)
    
    unknown = background - sure_fg
    show(unknown)


    ################
    # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)
    # Add one to all labels so that sure background is not 0, but 1
    markers = markers+1
    # Now, mark the region of unknown with zero
    markers[unknown==255] = 0

    markers = cv2.watershed(img, markers)
    img[markers == -1] = [255,0,0]
    show(img)

    return

def main():

    img = cv2.imread("imagens/img_cells.jpg")

    # watershed(img)

    binary_img = binarization(img)
    # show(binary_img)

    # get_areas(binary_img)

    # filled = fill_holes(img)
    filled = fill_holes(binary_img)
    # show(filled)

    # watershed(binary_neg)

main()