import cv2
import numpy as np
from PIL import Image
import re

CHAR_HEIGHT = 25
CHAR_WIDTH = 8.5
NB_LIGNES = 0
LAST_ORG_i = 0
LAST_ORG_j = 20


def int_to_bin(grayscale):
    return f'{grayscale:08b}'
            
def int_to_bin16(ycrcb):
    y, cr, cb = ycrcb
    return f'{y:016b}', f'{cr:016b}', f'{cb:016b}'

def bin_to_int(bgr):
    b, g, r = bgr
    return (int(b, 2),
            int(g, 2),
            int(r, 2))

def bin_to_int8(bgr):
    return (int(bgr, 2))

def merge_bgr(ycrcb, grayscale):
    y, cr, cb = ycrcb
    bgr = (y[0:12] + grayscale[0:4] ,
            cr[0:14] + grayscale[4:6] ,
            cb[0:14] + grayscale[6:8] ,
        )

    return bgr


# Transforme le texte en une image 8 bits
def text_to_image(texte, img_shape):
    global NB_LIGNES
    img_b = np.zeros(img_shape) # création d'une image vide avec la meme taille que l'image encoder
    h , w, _ = img_b.shape

    # Taille approximative d'un caractère dans l'image
    char_height = CHAR_HEIGHT
    char_width = CHAR_WIDTH

    org = (0, 20) # position initial du texte sur l'image

    texte_len = len(texte)
    nb_characters= int( w // char_width) # nombre de caractères sur une ligne

    i=0
    while i < texte_len: # tant qu'on a pas écrit l'integratlité du texte sur l'image
        # Dans le cas ou le texte restant à écricre possède moins de caractère que la limite de cactère
        # par ligne imposé on écrit l'intégralité du texte restant sur cette ligne
        if i + nb_characters >= texte_len:
            cv2.putText(img_b, texte[i:], org, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 55, 230), 2, cv2.LINE_AA)
            i += nb_characters #on positione l'indice a la fin de la phrase pour stoper la boucle

        else:
            space = nb_characters
            # Dans le cas ou le caractère finissant la ligne n'est pas un espace on retourne au dernier espace
            # existant afin de ne pas couper de mots lors de l'écriture sur cette ligne
            if texte[i + nb_characters] != " ": 
                while texte[i + space] != " " and space != 0:
                    space -= 1

                cv2.putText(img_b, texte[i: i + space + 1], org, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 55, 230), 2, cv2.LINE_AA)
                i += space + 1 # on pose l'indice sur le caractère se trouvant après le dernier espace détecté 

            else : # sinon on écrit directement le texte sur la ligne sans modifications 
                cv2.putText(img_b, texte[i: i + nb_characters], org, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 55, 230), 2, cv2.LINE_AA)
                i+=nb_characters # on pose l'indice sur le premier caractère non affiché

        org=(org[0], org[1] + char_height) # on effectue un saut a la ligne
        NB_LIGNES+=1

        cv2.imwrite(f'res2/text.png',img_b)

    return img_b

def encrypt(text, img_path):
    global LAST_ORG_j, LAST_ORG_i, NB_LIGNES, CHAR_HEIGHT,CHAR_WIDTH
    #convertir l'image principale et transformer son espace de couleurs
    img1 = cv2.imread(img_path, cv2.IMREAD_COLOR)
    img1 = np.uint16(img1)*255
    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2YCrCb)
    cv2.imwrite('res2/ycbcr.png',img1)
    if img1 is None: 
        print("image empty")
    else:
        text_to_image(text, img1.shape)
        img2 = cv2.imread('res2/text.png',cv2.IMREAD_COLOR)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('res2/gray.png',img2)
        # Create a new image 
        new_image = img1
        for i in range(img1.shape[0]):
            for j in range(img1.shape[1]):
                ycrcb = int_to_bin16(img1[i, j])
                bgr_text = int_to_bin(img2[i, j])
                # Merge the two pixels and convert it to a integer tupleshape
                bgr = merge_bgr(ycrcb, bgr_text)
                #for it in bgr:
                #    if not (re.fullmatch('[0]+', it[8:])):
                #        print(new_image[i, j])
                new_image[i, j] = bin_to_int(bgr) 

        new_image = cv2.cvtColor(new_image,cv2.COLOR_YCrCb2BGR)
        cv2.imwrite('res2/Final.png',new_image)

        LAST_ORG_i = LAST_ORG_i + CHAR_WIDTH*len(text)
        LAST_ORG_j = LAST_ORG_j + NB_LIGNES * CHAR_HEIGHT

    return new_image


def decrypt(new_img_path):
    img = cv2.imread(new_img_path, -1)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
    # Create the new image and load the pixel map
    new_image = np.zeros((img.shape[0], img.shape[1]), np.uint8)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            y, cr, cb = int_to_bin16(img[i, j])
            # Extract the last 8 bits (corresponding to the hidden image)
            ycrcb = (y[12:16]+ cr[14:16]+ cb[14:16])
            print(len(ycrcb))
            new_image[i, j] = bin_to_int8(ycrcb) 
            if (bin_to_int8(ycrcb) >170):
                new_image[i, j] =0
    k = np.zeros((img.shape[0], img.shape[1]), np.uint8)
    k= new_image[:int(LAST_ORG_j) , :int(LAST_ORG_i)] 
            
    cv2.imwrite('res2/Unmerged-Image.png',new_image)
    cv2.imwrite('res2/extracted_text.png',k)

    return new_image



if __name__ == '__main__':

    encrypt('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s', 'drias.jpg')
    decrypt('res2/Final.png')






