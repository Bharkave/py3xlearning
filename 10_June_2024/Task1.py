# 1.Explain the difference between the = operator and the == operator in Python.
# = operator is an assignment operator. It assigns value to a variable.
# == operator is a comparison operator used to compare the values between two variables . It will return only Boolean values as output.

a=5
b=5 # = is used to assign values to the respective variable
print(a==b)
# == It will compare both the values

# 2.What does the ** operator do in Python, and how is it used?
# ** it is exponentional operator ie: power operator . It returns power of given number

n=2
print(n**3)
# 2**3 , 2*2*2

# 3.What does the ^ operator do in Python, and in what context is it commonly used?
#The ^ operator in Python is a bitwise XOR operator.
#It follows XOR table. It compares the each bit of the first operand to the respective second operand.
#ie If one bit is 1 and other bit is 0 , it returns 1.

a=5
b=3
print(a^b)