import math



class Vertice:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure:
    name = ''


    def __init__(self):
        self.vertices = []

    def calc_length(self, v1: Vertice, v2: Vertice):
        d = math.sqrt((v2.x - v1.x) ** 2 + (v2.y - v1.y) ** 2)
        return d

    def calc_perimeter(self):
        sum = 0
        for i in range(len(self.vertices)):
            if i == len(self.vertices) - 1:
                sum = sum + self.calc_length(self.vertices[i], self.vertices[0])
            else:
                sum = sum + self.calc_length(self.vertices[i], self.vertices[i+1])
        return sum

    def calc_square(self):
        return 0.0

    # def add_square(self, figure):
    #     if not isinstance(value, type)
    #         raise TypeError("wrong type file")
    #     return self.calc_square() + figure.calc_square()


class Triangle(Figure):
        def __init__(self, v1: Vertice, v2: Vertice, v3: Vertice):
            super().__init__()
            self.vertices.append(v1)
            self.vertices.append(v2)
            self.vertices.append(v3)

        def calc_square(self):
            l1 = self.calc_length(self.vertices[0],self.vertices[1] )
            l2 = self.calc_length(self.vertices[1],self.vertices[2] )
            l3 = self.calc_length(self.vertices[2],self.vertices[0] )
            p = (l1 + l2 + l3) / 2
            h = (2 * math.sqrt(p * (p-l1) * (p-l2) * (p-l3))) / l1
            s = l1 * h * 0.5
            return s

class Rectangle(Figure):
        def __init__(self, v1: Vertice, v2: Vertice, v3: Vertice, v4: Vertice):
            super().__init__()
            self.vertices.append(v1)
            self.vertices.append(v2)
            self.vertices.append(v3)
            self.vertices.append(v4)

        def calc_square(self):
            l1 = self.calc_length(self.vertices[0], self.vertices[1])
            l2 = self.calc_length(self.vertices[1], self.vertices[2])
            return l1 * l2





tr = Triangle(Vertice(1,2),Vertice(3,5), Vertice(3,8))
# tr2 = Triangle(Vertice(1,4),Vertice(2,6), Vertice(8,9))
rec = Rectangle(Vertice(1,1),Vertice(1,3), Vertice(3,3), Vertice(3,1))

print(tr.calc_square())
print(rec.calc_square())

print(tr.add_square(rec))
