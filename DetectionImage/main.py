from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def rgbToYCbCr(image) :
    # Récup de la matrice de pixel
    pix_val = list(image.getdata())
    newMatrice = pix_val
    j = 0
    for i in pix_val :   #i représente chaque tuple
        Y = 0.257*i[0] + 0.504*i[1] + 0.098*i[2] + 16
        Cb = -0.148*i[0] - 0.291*i[1] + 0.439*i[2] + 128
        Cr = 0.439*i[0] - 0.368*i[1] + 0.071*i[2] + 128
        newMatrice[j] = (Y,Cb,Cr)
        j += 1
    return newMatrice

def difference(matrice, matriceCopy):
    matriceDif = list()
    j = 0
    for i in range(len(matrice)):
        difY = pow(abs(matrice[j][0] - matriceCopy[j][0]), 3)
        difCb = pow(abs(matrice[j][1] - matriceCopy[j][1]), 3)
        difCr = pow(abs(matrice[j][2] - matriceCopy[j][2]), 3)
        prod = difY+difCb+difCr
        matriceDif.append(prod)
        j += 1
    return matriceDif

def quedesZeros(matrice):
    for i in matrice:
        if i != (0.0, 0.0, 0.0):
            print(matrice)
            return False
    return True

def arrondi(matrice):
    j = 0
    for i in matrice:
        matrice[j] = (round(i))
        j += 1

def createRGBMatrice(matrice):
    matPix = list()
    for i in matrice:
        if i == 0:
            matPix.append((0,0,0))
        else :
            matPix.append((255,255,255))
    return matPix

def createImage(dubiousImage, matPix):
    width, height = dubiousImage.size
    i = 0
    for cptwidth in range (height):
        for cptheight in range (width):
            dubiousImage.putpixel((cptheight, cptwidth),matPix[i])
            i += 1
    dubiousImage.show()


#Ouverture de l'image
dubiousImage = Image.open("D:\Cours_IUT\\2A\MathsMod\DetectionImage\Images\Wntogd.jpg")


#D:\Cours_IUT\\2A\MathsMod\DetectionImage\Images\Clipsou.jpg
#D:\Cours_IUT\\2A\MathsMod\DetectionImage\Images\\archive\\real_and_fake_face\\training_fake\easy_16_1111.jpg
#D:\MAMP\htdocs\Animes\The_7_Deadly_Sins\merlin.jpg
#D:\Cours_IUT\\2A\MathsMod\DetectionImage\Images\htph50.jpg
#D:\Cours_IUT\\2A\MathsMod\DetectionImage\Images\ch10.jpg
#D:\Cours_IUT\\2A\MathsMod\DetectionImage\Images\\bilbo.jpg
#D:\Cours_IUT\\2A\MathsMod\DetectionImage\Images\Wntogd.jpg


#Conversion de la matrice RGB en matrice YCbCr
MatriceY = rgbToYCbCr(dubiousImage)

#Boucle pour changer la qualité de compression
i = 30
while i < 100:

    #copies de l'image
    original = dubiousImage.copy()
    copyImage = dubiousImage.copy()
    #Compression JPEG avec une qualité de compression
    copyImage.save("imgggg.jpeg","JPEG", quality=i)
    copyImage = Image.open("imgggg.jpeg")

    # Conversion de la matrice RGB en matrice YCbCr
    MatriceCopy = rgbToYCbCr(copyImage)

    #Diffférence des 2 matrices
    matriceDiff = difference(MatriceY, MatriceCopy)
    arrondi(matriceDiff)

    #Recréer une matrice de pixel grâce à la matrice de différence
    matPix = createRGBMatrice(matriceDiff)

    #Recréer l'image grâce à la matrice de pixel
    createImage(original, matPix)
    i += 2
    copyImage.close()
