import cv2
import numpy as np
from matplotlib import pyplot as plt


def show(img):

    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def binarization(img):

    # kernel = np.ones((5,5),np.uint8)

    ret, binary_image = cv2.threshold(img, 20, 255, cv2.THRESH_BINARY)

    # binary_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

    return binary_image

def morph_operations(img):

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (100,100))

    opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    tophat = img - opened

    return tophat
    
def main():

    img = cv2.imread("imagens/morf_test.png")
    # show(img)

    # binary_img = binarization(img)
    # # show(binary_img)

    test = morph_operations(img)
    # show(test)

    binary_img = binarization(test)
    show(binary_img)

    result = reduce_noise(binary_img)
    # show(result)

main()