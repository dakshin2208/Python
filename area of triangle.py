#1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle.

def calculate_area(b,h):
    area=(1/2)*b*h
    print(area)


b=int(input("enter a breath of the triangle:"))
h=int(input("enter a height of the triangle:"))

calculate_area(b,h)
