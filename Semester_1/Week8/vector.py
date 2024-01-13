class Vector:
    def __init__(self, data=None):
        self._vector = data.copy() if data is not None else []

    def __str__(self):
        if self._vector:
            return '<' + ', '.join(map(lambda x: f'{x:.1f}', self._vector)) + '>'
        return "<>"

    def dim(self):
        if not self._vector:
            return 0
        return len(self._vector)

    def set(self, index, value):
        self._vector[index] = value

    def get(self, index):
        return self._vector[index]

    def add(self, other):
        if not isinstance(other, Vector):
            raise TypeError(
                "The 'other' argument must be an instance of Vector")
        if self.dim() != other.dim():
            raise ValueError("Vectors must have the same dimensions")
        return Vector([a + b for a, b in zip(self._vector, other._vector)])

    def scalar_product(self, scalar):
        return Vector([val*scalar for val in self._vector])

    def equals(self, other):
        if not isinstance(other, Vector):
            return False
        return self._vector == other._vector
