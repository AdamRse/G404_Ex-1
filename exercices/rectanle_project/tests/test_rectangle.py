from exercices.rectanle_project.geometry.rectangle import Rectangle

def test_rectangle_values(var1, var2):
    try:
        rectangle = Rectangle(var1, var2)
        return True
    except:
        return False

def unit_test_rectangle():
    values_test = [
        [3, 2, True]
        ,[-1, 2, False]
        ,[4, -4, False]
        ,[-4, 4, False]
        ,[4, 4, False]
        ,[5, "4", False]
        ,["2", "4", False]
        ,["2", 10, False]
    ]

    for test in values_test:
        if test[2] != test_rectangle_values(test[0], test[1]):
            print(test, "Test rejetté")
            return False

    return True
