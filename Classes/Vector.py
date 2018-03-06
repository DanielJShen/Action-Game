################################################################################
# You need the math library to compute the square root of a number.
# The method to be used is math.sqrt.

import math


################################################################################
# Classes

# The Vector class
class Vector:

    # Initialiser
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Returns a string representation of the vector
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    # Tests the equality of this vector and another
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Tests the inequality of this vector and another
    def __ne__(self, other):
        return not self.__eq__(other)

        # Returns a tuple with the point corresponding to the vector

    def getP(self):
        return (self.x, self.y)

    def getIntP(self):
        return (int(self.x), int(self.y))

    # Returns a copy of the vector
    def copy(self):
        return Vector(self.x, self.y)

    # Adds another vector to this vector
    def add(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __add__(self, other):
        return self.copy().add(other);

    # Negates the vector (makes it point in the opposite direction)
    def negate(self):
        return self.multiply(-1)

    def __neg__(self):
        return self.copy().negate()

    # Subtracts another vector from this vector
    def subtract(self, other):
        return self.add(-other)

    def __sub__(self, other):
        return self.copy().subtract(other)

    # Multiplies the vector by a scalar
    def multiply(self, k):
        self.x *= k
        self.y *= k
        return self

    def __mul__(self, k):
        return self.copy().multiply(k)

    def __rmul__(self, k):
        return self.copy().multiply(k)

    # Divides the vector by a scalar
    def divide(self, k):
        if k==0: return Vector(0,0)
        return self.multiply(1 / k)

    def __truediv__(self, k):
        return self.copy().divide(k)

    # Normalizes the vector
    def normalize(self):
        return self.divide(self.length())

    # Returns a normalized version of the vector
    def getNormalized(self):
        return self.copy().normalize()

    # Returns the dot product of this vector with another one
    def dot(self, other):
        return self.x * other.x + self.y * other.y

    # Returns the length of the vector
    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # Returns the angle with (1,0) in radians
    def direction(self):
        return math.acos(self.getNormalized().x)

    # Returns the squared length of the vector
    def lengthSquared(self):
        return self.x ** 2 + self.y ** 2

    def getNormal(self):
        return self.copy().getNormalized().rotAnti()

    # Reflect this vector on a normal
    def reflect(self, normal):
        n = normal.copy()
        n.multiply(2 * self.dot(normal))
        self.subtract(n)
        return self

    def rotAnti(self):
        aux = self.copy()
        self.x = -aux.y
        self.y = aux.x
        return self

    def getProj(self, normal):
        n = normal.copy()
        return n.multiply(self.dot(n))

    # Returns the angle between this vector and another one
    # You will need to use the arccosine function:
    # acos in the math library
    def angle(self, other):
        return math.acos(self.dot(other) / (math.ceil(self.length()*10000)/10000 * math.ceil(other.length()*10000)/10000))

    def angleToX(self):
        angle = math.atan2(self.y,self.x)
        if angle < 0:
            angle += 2*math.pi
        return angle