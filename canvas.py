import numpy as np
from PIL import Image


class Canvas:
    """
    creates a canvas with the specified dimensions and fill color
    """
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # Create a 3 numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # Change [0, 0, 0] with user given values
        self.data[:] = self.color

    def make(self, imagepath):
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)