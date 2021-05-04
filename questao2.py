import cv2
import numpy as np
from matplotlib import pyplot as plt

def show(img):

    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def binarization(img):

    kernel = np.ones((5,5),np.uint8)

    ret, binary_image = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    binary_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

    return binary_image

# checa se a imagem esá vazia. Se sim , retorna TRUE
def is_empty(img):

    h = img.shape[0]

    for i in range(h):
        if (np.sum(img[i]) != 0):
            return False

    return True

# calcula diametro dos cookies
def get_diameter(img):

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h = img.shape[0]

    arr = np.array([], dtype=np.int32)

    # soma todos os pixeis 255 de uma fileira da imagem
    #
    #   [255, 255, 0, 0, 255] = 255 + 255 + 255 = 765
    #   [ 0,  0,  0,  0,  0 ] = 0
    #   [ 0, 255, 0,  0,  0 ] = 255
    #
    # vai criar um array com o resultado das somas. arr = [765, 0, 255] no caso do exemplo acima
    for i in range(h):
        if (np.sum(img[i]) != 0):
            arr = np.append(arr, np.sum(img[i]))

    # diametro = maximo elemento do array /255 => (total de pixeis brancos)  dividido por dois cookies 
    diameter = int((max(arr)/255)/2)

    return diameter

# faz a erosao do cookie
def erode_image(img, diameter):

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (diameter,diameter))
    erode = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel)

    return erode

#eliminar a cookie mordida
def eliminate_cookie(img):

    diameter = get_diameter(img)

    erode = erode_image(img, diameter)

    #caso a imagem esteja vazia, diminui o diametro por 1, até deixar algum pixel na imagem
    while(is_empty(erode)):
        diameter -= 1
        erode = erode_image(img, diameter)

    return erode

# recuperar forma inicial da cookie na imagem binarizada
def recover(original_img, new_img):

    diameter = get_diameter(original_img)    
    diameter += int(0.15 * diameter)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (diameter,diameter))
    recovered_cookie = cv2.morphologyEx(new_img, cv2.MORPH_DILATE, kernel)
 
    return recovered_cookie

# usar imagem da funcao recupear como mascara para deixar so a cookie completa na imagem original
def alterar_imagem(img, mask):

    result = cv2.bitwise_and(img, mask)
    return result

def main():

    img = cv2.imread("imagens/cookies.tif")
    # show(img)

    binary_image = binarization(img)
    # show(binary_image)

    erode = eliminate_cookie(binary_image)
    # show(erode)

    recovered_cookie_mask = recover(binary_image, erode)
    # show(recovered_cookie_mask)

    result = alterar_imagem(img, recovered_cookie_mask)
    show(result)

main()