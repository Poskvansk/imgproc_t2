import cv2
import numpy as np
from matplotlib import pyplot as plt

def show(img):

    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def binarization(img):

    ret, binary_image = cv2.threshold(img, 25, 255, cv2.THRESH_BINARY)
    return binary_image

# faz o tophat da imagem
def morph_operations(img):

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (150,150))
    opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    tophat = img - opened

    return tophat
    
# faz a abertura para reduzir quaisquer pequenos ruídos, e unir regiões desconexas dos numeros
def reduce_noise(img):

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    denoised = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    return denoised

def main():

    img = cv2.imread("imagens/morf_test.png")
    # show(img)

    tophat = morph_operations(img)
    # show(tophat)
    
    binary_img = binarization(tophat)
    show(binary_img)
    
    result = reduce_noise(binary_img)
    show(result)
    
main()