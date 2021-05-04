import cv2
import numpy as np
from matplotlib import pyplot as plt

def show(img):

    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def binarization(img):

    ret,binary_img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
    return binary_img

# preence os espacos vazios no centro da célula
def fill_holes(img):
    
    negative = cv2.bitwise_not(img)
    aux = negative.copy()

    # abertura para reduzir ruídos
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    negative = cv2.morphologyEx(negative, cv2.MORPH_OPEN, kernel)

    # flood fill do fundo da imagem (preto) em branco
    cv2.floodFill(aux, None, (5,5), 255)

    # negativo de aux
    aux = cv2.bitwise_not(aux)


    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
    # negativo + aux = imagem com buracos preenchidos
    filled = cv2.bitwise_or(negative, aux)
    # fechamento para quaisquer pequenos buracos que tiverem sobrado
    filled = cv2.morphologyEx(filled, cv2.MORPH_CLOSE, kernel)

    return filled

def watershed(img):

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

    # encontra a área que certamente faz parte do fundo
    background = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernel, iterations=2)

    dist_transform = cv2.distanceTransform(img, cv2.DIST_L2, 3)

    # encontra a área que certamente faz parte das células
    ret, sure_cell = cv2.threshold(dist_transform,0.3*dist_transform.max(),255,0)
    sure_cell = np.uint8(sure_cell)

    # área incerta
    unknown = cv2.subtract(background, sure_cell)

    # cira os marcadores
    ret, markers = cv2.connectedComponents(sure_cell)
    markers = markers + 1
    markers[unknown==255] = 0

    # converte para o watershed
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    markers = cv2.watershed(img, markers)
    img[markers == -1] = [255,0,0]  

    # negativo para as células ficarem pretas no fundo branco
    img = cv2.bitwise_not(img)

    return img

def main():

    img = cv2.imread("imagens/img_cells.jpg",0)

    binary_img = binarization(img)

    filled = fill_holes(binary_img)

    segment = watershed(filled)
    # cv2.imwrite("cell-result.jpg", segment)
    show(segment)

main()