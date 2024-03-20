from PIL import Image
print("Vyber jeden z následujícíh souborů k úpravě:")
print("leiurus.jpg nebo poecilotheria.jpg")
x = input(": ")
obrazek = Image.open(x)
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

