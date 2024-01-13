"""Write a function that takes the lengths of the sides of a triangle (a, b, and c) from the user and
then print the area of the triangle using Heron's formula"""

def herons(a,b,c):
    a,b,c = float(a),float(b),float(c)
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    return area

a = input("Enter side lenght 1: ")
b = input("Enter side lenght 2: ")
c = input("Enter side lenght 3: ")

print(round(herons(a,b,c),3))
