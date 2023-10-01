# geometry module: geom.py
class Rectangle: # rectangle class
    # make a rectangle using top left and bottom right coordinates
    def __init__(self,tl,br):
        self.tl=tl #setting the variables
        self.br=br
        self.width=abs(tl.x-br.x)  # width - this maths is new to me
        self.height=abs(tl.y-br.y) # height
    def area(self): # gets area of rectangle
        return self.width*self.height

class Coordinate: # coordinate class
     def __init__(self,x,y):
        # make coordinate obj with a reference (self), an x and a y
        self.x=x
        self.y=y
     def distance(self,another): # distance between 2 coordinates
        import math
        xdist=abs(self.x-another.x)
        ydist=abs(self.y-another.y)
        return math.sqrt(xdist**2+ydist**2) # pythagoras theorem
     
def test():
    p1 = Coordinate(1,1)
    p2 = Coordinate(4,5)
    dist = p1.distance(p2)
    print(f"I expect this to be 5, and it's actual distance is {dist}")

    rec = Rectangle(p1,p2)
    area = rec.area()
    print(f"I expect this to be 12cm2, and it's actual area is {area}cm2")

test()