def scalar_product(scalar, vector):
    new_vector = []
    for num in vector:
        new_vector.append(num*scalar)
    return new_vector

print(scalar_product(5,[1,2,3,-4]))

def vector_add(vector1, vector2):
    new_vector = []
    for num1,num2 in zip(vector1,vector2):
        new_vector.append(num1+num2)
    return new_vector

print(vector_add([1,2,3,-2],[3,2,1,2]))

class Vector:
    def __init__(self,value):
        self.value = value

    def __add__(self,other):
        new_vector = []
        for num1,num2 in zip(self.value,other.value):
            new_vector.append(num1+num2)
        return new_vector
    
    
    
    def scalar_mult(self, scalar):
        new_vector = []
        for num in self.value:
            new_vector.append(num*scalar)
        return new_vector


vect_a = Vector([1,2,3])

vect_a.scalar_mult(3)

print(vect_a)

vect_b = Vector([4,3,2])

vect_c = vect_a + vect_b

print(vect_c)
    
