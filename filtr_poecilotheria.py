from PIL import Image
obrazek = Image.open("poecilotheria.jpg")
sirka, vyska = obrazek.size
def uprava_barev():
    x = 0    
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x,y))
            prumer = int((r+g+b)/2.4)
            obrazek.putpixel((x,y), (r , b, r))
            if prumer > 150:
                obrazek.putpixel((x,y), (255, 255, 255))
            else:
                obrazek.putpixel((x,y), (100, 130, 90))
            y += 1
        x += 1
    obrazek.show()
# display(obrazek) #obrazek.show()
uprava_barev()