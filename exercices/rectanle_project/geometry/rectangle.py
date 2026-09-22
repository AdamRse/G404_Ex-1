class Rectangle:

    height = 1
    width = 1

    def __init__(self, width:int, height:int):
        if (width == height):
            raise ValueError("Les dimensions ne doivent pas être égales.")
        if width <= 0 or height <= 0:
            raise ValueError("Les dimensions doivent être strictement positives.")
        self.width = width
        self.height = height

    def area(self, text_print = False):
        calc_area = self.width * self.height
        if text_print:
            print(f"Hauteur : {self.height}, largeur : {self.width}")
            print(f"L'aire du rectangle est de {calc_area}")
        return calc_area

    def update_width(w:int):
        self.width = w

    def update_height(h:int):
        self.height = h
