import math

class Point:
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
    def show(self):
        print(self.x1, self.y1)
    def move(self, x2, y2):
        self.x2 = x2
        self.y2 = y2
    def dist(self, difx, dify):
        difx = (self.x2 - self.x1)**2
        dify = (self.y2 - self.y1)**2
        return math.sqrt(difx + dify)
        
x = int(input())
y = int(input())
A = Point(x, y)
A.show()
x2 = int(input())
y2 = int(input())
A.move(x2,y2)
print(A.dist(x,y))