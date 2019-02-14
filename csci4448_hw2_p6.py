class Point:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    # getters for coordinates of the point
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    def __str__(self):
        return "(%s,%s)" % (self.x,self.y)
    # Rotates point 90 deg counterclockwise about point c and returns the resulting point
    def rot90deg(self,c):
        return Point(c.x-self.y+c.y,c.y+self.x-c.x)
    

class Shape:
    def __init__(self,z):
        self.__z = z
    # getter for z-value of the shape
    @property
    def z(self):
        return self.__z
    def __str__(self):
        return "Shape"

class Circle(Shape):
    def __init__(self,z,cx,cy,r):
        super().__init__(z)
        self.__c = Point(cx,cy)
        self.__r = r;
    def __str__(self):
        return "Circle with center %s and radius %s" % (self.__c,self.__r)

class Triangle(Shape):
    def __init__(self,z,v1x,v1y,v2x,v2y,v3x,v3y):
        super().__init__(z)
        self.__v1 = Point(v1x,v1y)
        self.__v2 = Point(v2x,v2y)
        self.__v3 = Point(v3x,v3y)
    def __str__(self):
        return "Triangle with vertices %s, %s, and %s" % (self.__v1,self.__v2,self.__v3)

class Square(Shape):
    def __init__(self,z,cx,cy,vx,vy):
        super().__init__(z)
        c = Point(cx,cy)
        self.__v1 = Point(vx,vy)
        self.__v2 = self.__v1.rot90deg(c)
        self.__v3 = self.__v2.rot90deg(c)
        self.__v4 = self.__v3.rot90deg(c)
    def __str__(self):
        return "Square with vertices %s, %s, %s, and %s" % (self.__v1,self.__v2,self.__v3,self.__v4)


database = (
    ("Circle",3,4,5,6),
    ("Triangle",4,1,2,3,5,7,3),
    ("Square",2,5,7,3,5)
)

def getShape(entry):
    if entry[0] == "Circle":
        return Circle(entry[1],entry[2],entry[3],entry[4])
    if entry[0] == "Triangle":
        return Triangle(entry[1],entry[2],entry[3],entry[4],entry[5],entry[6],entry[7])
    if entry[0] == "Square":
        return Square(entry[1],entry[2],entry[3],entry[4],entry[5])

def main():
    shapes = [getShape(entry) for entry in database]
    # sort by z-value of each shape
    shapes.sort(key=lambda s:s.z)
    for shape in shapes:
        print(shape)

main()
