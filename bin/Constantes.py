from PIL  import ImageTk, Image
newsize = (100,100)
im1 = Image.open("./imagenes/papel.jpg")
imagen_papel = im1.resize(newsize)
im2 = Image.open("./imagenes/piedra.jpg")
imagen_piedra = im2.resize(newsize)
im3 = Image.open("./imagenes/Tijera.jpg")
imagen_tijera = im3.resize(newsize)
