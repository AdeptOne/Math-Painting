class Square:
    """
    creates a square at the specified x, y coordinates
    with the given side size and color.
    """
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        canvas.data[self.y: self.y + self.side + 1, self.x:self.x + self.side + 1] = self.color


class Rectangle:
    """
    creates a rectangle at the specified
    x, y coordinates with the given dimensions and color
    """
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        canvas.data[self.y:self.y + self.height + 1, self.x:self.x + self.width + 1] = self.color

    def area(self):
        return self.height * self.width