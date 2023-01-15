from PIL import Image

i = Image.open("Imagetest.bmp")
sortie = i.copy()

for y in range(i.size[1]):
    for x in range(i.size[0]):
        c = i.getpixel((x,y))
        sortie.putpixel((y,x),c)

sortie.save("Imageout.bmp")


i = Image.open("hall-mod_0.bmp")
sortie = i.copy()

for y in range(i.size[1]):
    for x in range(i.size[0]):
        c = i.getpixel((i.size[0]-x-1,y))
        sortie.putpixel((x,y),c)

sortie.save("Imageout1.bmp")

i = Image.open("IUT-Orleans.bmp")
sortie = i.copy()

for y in range(i.size[1]):
    for x in range(i.size[0]):
        R,V,B = i.getpixel((x,y))
        Gris=int((R+V+B)/3)
        sortie.putpixel((x,y),(Gris,Gris,Gris))

sortie.save("Imageout2.bmp")


i = Image.open("IUT-Orleans.bmp")
sortie = i.copy()

for y in range(i.size[1]):
    for x in range(i.size[0]):
        R,V,B = i.getpixel((x,y))
        if (R*R+V*V+B*B)>255*255*3/2:
            sortie.putpixel((x,y),(255,255,255))
        else:
            sortie.putpixel((x,y),(0,0,0)) 

sortie.save("Imageout3.bmp")



def cacher(i,b):
    return i-(i%2)+b

i = Image.open("hall-mod_0.bmp")
j = Image.open("Imageout3.bmp")
sortie = i.copy()

for y in range(i.size[1]):
    for x in range(i.size[0]):
        R,V,B = i.getpixel((x,y))
        c = j.getpixel((x,y))
        if c == (255,255,255):
            a = 1
        else:
            a = 0
        sortie.putpixel((x,y),(cacher(R,a),V,B))


sortie.save("Imageout_steg_1.bmp")


def trouver(i):
    return i%2

i = Image.open("Imageout_steg_1.bmp")
sortie = i.copy()

for y in range(i.size[1]):
    for x in range(i.size[0]):
        R,V,B = i.getpixel((x,y))
        couleur=trouver(R)*255
        sortie.putpixel((x,y),(couleur,couleur,couleur))


sortie.save("Imageout_steg_2.bmp")