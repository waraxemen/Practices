class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height
    def getArea(self): #рассчёт площади
        return self.width*self.height
class Square:#Square (квадрат), который принимает в качестве аргумента одну сторону
    def __init__(self,a):
        self.a=a
    def get_area_square(self):
            return self.a**2
class Circle:
    def __init__(self, radius):
        self.radius=radius
    def areaCircle(self):
        return 3.1416* self.radius**2