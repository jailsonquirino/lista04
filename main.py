from PIL import Image, ImageFilter

imagemoriginal = Image.open('imagens/casa1.jpg')

kernel1 = ImageFilter.Kernel((3,3), (1,0,-1,0,0,0,-1,0,1), 1, 0)
kernel2 = ImageFilter.Kernel((3,3), (0,1,0,1,-4,1,0,1,0), 1, 0)
kernel3 = ImageFilter.Kernel((3,3), (-1,-1,-1,-1,8,-1,-1,-1,-1), 1, 0)

img1 = imagemoriginal.filter(kernel1)
img2 = imagemoriginal.filter(kernel2)
img3 = imagemoriginal.filter(kernel3)

img1.save('imagens/casa1filtro1.jpg')
img2.save('imagens/casa1filtro2.jpg')
img3.save('imagens/casa1filtro3.jpg')

imagemoriginal2 = Image.open('imagens/ponte.jpg')

kernel4 = ImageFilter.Kernel((3,3), (0,-1,0,-1,5,-1,0,-1,0), 1, 0)
kernel5 = ImageFilter.Kernel((3,3), (1/9,1/9,1/9,1/9,1/9,1/9,1/9,1/9,1/9), 1, 0)

img4 = imagemoriginal2.filter(kernel4)
img5 = imagemoriginal2.filter(kernel5)

img4.save('imagens/pontesharpen.jpg')
img5.save('imagens/boxblur.jpg')


