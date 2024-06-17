n1=int(input("Enter the first side of triangle in cms:\t"))
n2=int(input("Enter the first side of triangle in cms:\t"))
n3=int(input("Enter the first side of triangle in cms:\t"))
if n1==n2==n3:
    print("The triangle is equilateral")
elif (n1==n2) or (n2==n3) or (n1==n3):
    print("The triangle is Isosceles")
else:
    print("The triangle is Scalene")