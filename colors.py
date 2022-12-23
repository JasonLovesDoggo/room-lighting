

class Color:
    def __init__(self, R: int, G: int, B: int):
        self.R = R
        self.G = G
        self.B = B
        print(f"Color: {self}")

    def __str__(self):
        return f"R: {self.R}, G: {self.G}, B: {self.B}"

    def __repr__(self):
        return f"R: {self.R}, G: {self.G}, B: {self.B}"


RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
PURPLE = Color(248, 207, 255)
