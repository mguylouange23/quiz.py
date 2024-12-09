import math

class Point:
    def __init__(self,x,y):
        ''' Initialize the point instance'''
        self.x=x
        self.y=y
        #your code goes here
    def get_x(self):
        ''''Getter for the x coordinate'''
        return self.x
        #your code goes here
    def get_y(self):
        '''Getter for the y coordinate'''
        return self.y
        #your code goes here
    def set_x(self,x):
        '''Setter for the x coordinate'''
        if x<0:
            raise ValueError('x cant be negative')
        self.x=x
        #your code goes here
    def set_y(self,y):
        '''Setter for the y coordinate'''
        if y<0:
            raise ValueError("y cant be negative")
        self.y=y
        #your code goes here
    def distance(self,other):
        '''Calculate the distance between two points'''
        d_x= ((self.x)-(other.x))**2
        d_y=((self.y)-(other.y))**2
        return math.sqrt(d_x+d_y)
        #your code goes here
    def __eq__(self,other):
        '''Two points are equal if they have the same x and y coordinates'''
        return  ((self.x ==other.x) and (self.y == other.y))
        #your code goes here
    def __str__(self):
        ''''Returns a string representation of the point as (x,y)'''
        return f"({self.x},{self.y})"
        #your code goes here

class Circle: 
    def __init__(self,center,radius):
        ''' Initialize the circle instance raise a ValueError exception
        if the radius is not a positive number or center is not a point object'''
        if not isinstance(center, Point):
            raise ValueError("Center must be a Point object")
        if radius <= 0:
            raise ValueError("Radius must be a positive number")
        self.center = center
        self.radius = radius
        #your code goes here
    def get_center(self):
        '''Getter for the center of the circle'''
        return self.center
        #your code goes here
    def get_radius(self):
        '''Getter for the radius of the circle'''
        return self.radius
        #your code goes here
    def set_center(self,center):
        '''Setter for the center of the circle'''
        if not isinstance(center, Point):
            raise ValueError("Center must be a Point object")
        self.center = center
        #your code goes here
    def set_radius(self,radius):
        '''Setter for the radius of the circle'''
        if radius <= 0:
          raise ValueError("Radius must be a positive number")
        self.radius = radius
        #your code goes here
    def area(self):
        '''Calculate the area of the circle'''
        return math.pi * self.radius ** 2
        #your code goes here
    def __str__(self):
        '''Returns a string representation of the circle as Center:(x,y), Radius: r'''
        return f"Center: {self.center}, Radius: {self.radius}"
        #your code goes here  
    def is_in(self,point):
        '''Check if a point is inside the circle'''
        if not isinstance(point, Point):
            raise ValueError("The point must be a Point object")
        distance_from_center = self.center.distance(point)
        return distance_from_center < self.radius

        #your code goes here
    def __eq__(self,other):
        '''Two circles are equal if they have exactly the same center and the same radius''' 
        return self.center == other.center and self.radius == other.radius
        #your code goes here


origin=Point(0,0)
p1=Point(3,4)
p2=Point(2,3)
c1=Circle(origin,4)
c2=Circle(p1,3)
print(c1)
print(p1)
print(c1.area())
print(c1.is_in(p1))
print(c2.is_in)
