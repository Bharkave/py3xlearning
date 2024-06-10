# Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8
n=2
square_of_the_number = n**2
cube_of_the_number = n**3
print("The square of the number is : ",square_of_the_number)
print("The cube of the number is : ",cube_of_the_number)

#Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
n1 = int(input("Enter the first number :"))
n2 = int(input("Enter the second number :"))
if(n1>n2):
    print("n1 is greater than n2")
elif(n1<n2):
    print("n1 is smaller than n2")
else:
    print("n1 is equals to n2")