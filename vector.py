from math import sqrt

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        new_coordinates = [x + y for x, y in zip(self.coordinates, v)]
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x - y for x, y in zip(self.coordinates, v)]
        return Vector(new_coordinates)

    def times_scalar(self, scalar):
        new_coordinates = [x * scalar for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        return sqrt(sum(map(lambda x: (x*x), self.coordinates)))

    def unit(self):
        normalized = 1.0/self.magnitude()
        return self.times_scalar(normalized)
