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

    kernel = np.ones((5,5),np.uint8)

    ret, binary_image = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    binary_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

    return binary_image

def is_empty(img):
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    h = img.shape[0]

    for i in range(h):
        if (np.sum(img[i]) != 0):
            return False

    return True

def get_diameter(img):

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h = img.shape[0]

    arr = np.array([], dtype=np.int32)

    for i in range(h):
        if (np.sum(img[i]) != 0):
            arr = np.append(arr, np.sum(img[i]))

    diameter = int((max(arr)/255)/2) -1

    return diameter

def eliminate_cookie(img, diameter):

    #eliminar a cookie mordida

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (diameter,diameter))

    erode = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel)

    return erode

def erode_image(img):

    diameter = get_diameter(img)

    erode = eliminate_cookie(img, diameter)

    while(is_empty(erode)):
        diameter -= 1
        erode = eliminate_cookie(img, diameter)

    return erode

def recuperar(original_img, new_img):

    #recuperar forma inicial da cookie na imagem binarizada

    diameter = get_diameter(original_img)
    
    diameter += int(0.15 * diameter)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (diameter,diameter))

    recovered_cookie = cv2.morphologyEx(new_img, cv2.MORPH_DILATE, kernel)
 
    return recovered_cookie

def alterar_imagem(img, mask):

    # usar imagem da funcao recupear como mascara para deixar so a cookie completa na imagem original

    result = cv2.bitwise_and(img, mask)

    return result


def main():

    img = cv2.imread("imagens/cookies.tif")
    # show(img)

    binary_image = binarization(img)
    # show(binary_image)

    erode = erode_image(binary_image)
    # show(erode)

    recovered_cookie_mask = recuperar(binary_image, erode)
    # show(recovered_cookie_mask)

    result = alterar_imagem(img, recovered_cookie_mask)
    show(result)


main()