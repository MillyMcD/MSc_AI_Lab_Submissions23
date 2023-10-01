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
