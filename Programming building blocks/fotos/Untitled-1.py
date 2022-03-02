from PIL import Image

image_original = Image.open("earth.jpg")
image_original.show()
width, height = image_original.size
pixels_original = image_original.load()
r, g, b = pixels_original[255,255]
pixels_original[100, 200] = (r, g, b)
image_original.save("the_file_goes_here.jpg")