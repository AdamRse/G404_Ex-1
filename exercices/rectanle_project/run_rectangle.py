from exercices.rectanle_project.tests.test_rectangle import unit_test_rectangle
from exercices.rectanle_project.geometry.rectangle import Rectangle

def main():
    if unit_test_rectangle():
        print("Test réussis !")
    else:
        print("Les tests ont échoués")
        return False
    rect = Rectangle(2, 5)
    rect.area(True)
