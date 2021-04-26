import cv2
import numpy as np
from matplotlib import pyplot as plt

def show(img):

    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # plt.imshow(img[:,:,::-1]); plt.show()
    # plt.imshow(img, cmap='gray', vmin=0, vmax=255); plt.show()


def morfologico(img):

    #CRIAR OPERACAO MORFOLOGICA PRA MELHORAR BINARIZACAO DA IMAGEM

    return

def binarization(img):

    ret,thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    show(thresh)

    # img = cv2.medianBlur(img, 5)
    
    # # th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)    
    # # show(th2)

    # th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    # show(th2)

    # th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
    # show(th3)


def main():

    img = cv2.imread("imagens/morf_test.png")
    # show(img)
    binarization(img)

main()