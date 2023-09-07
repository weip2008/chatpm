import math
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def rotate(self, theta):
        cos_theta = math.cos(theta)
        sin_theta = math.sin(theta)
        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta
        self.x = new_x
        self.y = new_y

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy


class Triangle:
    def __init__(self, p1=Point(), p2=Point(), p3=Point(), color='blue'):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.color = color
        self.plot = 5

    def rotate(self, theta):
        self.p1.rotate(theta)
        self.p2.rotate(theta)
        self.p3.rotate(theta)

    def translate(self, dx, dy):
        self.p1.translate(dx, dy)
        self.p2.translate(dx, dy)
        self.p3.translate(dx, dy)

    def plot(self): # override the self.plot attribute
        plt.plot([self.p1.x, self.p2.x], [self.p1.y, self.p2.y], color=self.color)
        plt.plot([self.p2.x, self.p3.x], [self.p2.y, self.p3.y], color=self.color)
        plt.plot([self.p3.x, self.p1.x], [self.p3.y, self.p1.y], color=self.color)

    def plot(self, color='red'): # override previous self.plot() function
        x = [self.p1.x,self.p2.x,self.p3.x,self.p1.x,]
        y = [self.p1.y,self.p2.y,self.p3.y,self.p1.y,]
        plt.plot(x,y)

# Create a triangle and plot it
t = Triangle(Point(1, 1), Point(3, 1), Point(2, 3))
t.plot()

# Rotate the triangle and plot it again
theta = math.pi / 4  # Rotate by 45 degrees
t.rotate(theta)
t.color = 'red'
t.plot()

# Show the plot
plt.axis('equal')
plt.show()
