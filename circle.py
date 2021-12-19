class Circle:

    def __init__(self, x, y, r):
        self.upper_border = y + r
        self.left_border = x - r
        self.right_border = x + r
        self.lower_border = y - r
