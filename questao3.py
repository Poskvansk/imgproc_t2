import cv2
import numpy as np
from matplotlib import pyplot as plt


def show(img):

    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # plt.imshow(img[:,:,::-1]); plt.show()
    # plt.imshow(img, cmap='gray', vmin=0, vmax=255); plt.show()


def binarization(img):

    img = cv2.medianBlur(img, 5)
    ret,thresh = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)
    show(thresh)


def preencher(img):

    # preencher espaco das celulas
    return


def segmentacao_watersheed(img):

    # usar imagem da funcao recupear como mascara para deixar so a cookie completa na imagem original

    return


def main():

    img = cv2.imread("imagens/img_cells.jpg")
    # show(img)
    binarization(img)

main()