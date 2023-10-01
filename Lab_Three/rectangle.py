# module name rectangle.py

class Rectangle: # Rectangle class
    # init method accepts width and height of Rectangle
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    #perimeter method retuns the perimeter of the rectangle
    def perimeter(self):
        return 2*(self.__width + self.__height)

    #perimeter method retuns the area of the rectangle
    def area(self):
        return self.__width * self.__height

def test_area():
    print("Testing area method")
    rect = Rectangle(12,4)
    actual = rect.area()
    print("area of a rectangle of width 12 and height 4 is expected to be 48")
    print(f"actual result {actual}")

def test_perimeter():
    print("Testing perimeter method")
    rect = Rectangle (12,4)
    actual = rect.perimeter()
    print ("Perimeter of a rectangle of width 12 and height 4 is expected to be 32")
    print (f'Actual result {actual}')

def main():
    test_area()
    print("")
    test_perimeter()

main()