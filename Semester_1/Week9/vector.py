class Vector:
    def __init__(self, *args):
        if not args:
            self._vector = []
        elif isinstance(args[0], list):
            self._vector = args[0].copy()
        else:
            self._vector = list(args)

    def get_vv(self):
        return self._vector

    def __str__(self):
        if self._vector:
            return '<' + ', '.join(map(lambda x: f'{x:.1f}', self._vector)) + '>'
        return "<>"

    def dim(self):
        if not self._vector:
            return 0
        return len(self._vector)

    def __setitem__(self, index, value):
        self._vector[index] = value

    def __getitem__(self, index):
        return self._vector[index]

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError()
        if self.dim() != other.dim():
            raise ValueError("Vectors must have the same dimensions")
        return Vector([a + b for a, b in zip(self._vector, other._vector)])

    def __iadd__(self, other):
        return self.__add__(other)

    def __mul__(self, scalar):
        raise TypeError(
            "Unsupported operand type: Vector can only be multiplied by a scalar from the right")

    def __rmul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError(
                "Unsupported operand type: Vector can only be multiplied by a scalar from the right")
        return Vector([val*scalar for val in self._vector])

    def __imul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError(
                "Unsupported operand type: Vector can only be multiplied by a scalar")
        self._vector = [val*scalar for val in self._vector]
        return self

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self._vector == other._vector

    def __ne__(self, other):
        return not self.__eq__(other)


a = Vector([1, 2, 3])
b = Vector(1, 2, 3)
