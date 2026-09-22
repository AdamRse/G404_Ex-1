class Duration:

    minutes = 0 # Optionel

    def __init__(self, minutes:int): # Optionel
        self.minutes = minutes

    def show_minutes(self):# self obligatoire, il n'est pas donné à l'utilisation de la méthode
        print(f"La durée est de {self.minutes} minute" + ("s" if self.minutes > 1 else ""))

    def add_duration(self, minutes:int):
        self.minutes += minutes

class Rectangle:

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

def main():
    obj = Duration(1)
    obj.show_minutes()
    obj.add_duration(4)
    obj.show_minutes()
