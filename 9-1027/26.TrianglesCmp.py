import math
class Triangle:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = float(x), float(y), float(z)

    def __bool__(self):
        if self.x + self.y > self.z and self.x + self.z > self.y and self.y + self.z > self.x and self.x > 0 and self.y > 0 and self.z > 0:
            return True
        else:
            return False

    def __abs__(self):
        if not self:
            return 0
        else:
            s = (self.x + self.y + self.z)/2
            area = math.sqrt(s*(s - self.x)*(s - self.y)*(s - self.z))
            return area

    def __str__(self):
        return f"{self.x}:{self.y}:{self.z}"

    def __eq__(self, other):
        if math.isclose(abs(self),abs(other)):
            self_list = sorted([self.x, self.y, self.z])
            other_list = sorted([other.x, other.y, other.z])
            return self_list == other_list
        else:
            return False

    def __lt__(self, other):
        if abs(self) < abs(other):
            return True
        else:
            return False

    def __le__(self, other):
        if abs(self) < abs(other) or abs(self) == abs(other):
            return True
        else:
            return False

    def __gt__(self, other):
        if abs(self) > abs(other):
            return True
        else:
            return False

    def __ge__(self, other):
        if abs(self) > abs(other) or abs(self) == abs(other):
            return True
        else:
            return False

# tri = Triangle(3, 4, 5), Triangle(5, 4, 3), Triangle(7, 1, 1), Triangle(5, 5, 5), Triangle(7, 4, 4)
# for a, b in zip(tri[:-1], tri[1:]):
#     print(a if a else b)
#     print(f"{a}={abs(a):.2f} {b}={abs(b):.2f}")
#     print(a == b)
#     print(a >= b)
#     print(a < b)