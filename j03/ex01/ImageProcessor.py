import numpy as np
from matplotlib import pyplot as PLT

class ImageProcessor:
    def load(self, path):
        image = PLT.imread(path)
        if len(image[0][0]) == 3:
            lon, lar = len(image), len(image[0])
            print(f"Size of the image : {lon} x {lar}")
            return image

    def display(self, array):
        PLT.imshow(array)
        PLT.axis("off")
        PLT.show()

image = ImageProcessor()
array = image.load("image1.png")
image.display(array)
