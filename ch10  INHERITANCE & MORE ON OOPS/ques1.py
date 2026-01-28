class TwoDVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def display(self):
        return f"2D Vector: ({self.x}, {self.y})"

class ThreeDVector(TwoDVector):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    def display(self):
        return f"3D Vector: ({self.x}, {self.y}, {self.z})"

o=TwoDVector(3,4)
print(o.display())
p=ThreeDVector(5,6,7)
print(p.display())



