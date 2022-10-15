'''
Here instead of using several if/else conditional statements for compairing each pair of numbers,
it just uses the nested function concept to find out the result using the previous function.
'''
def max_of_two(x,y):
  if x>y:
    return x
  return y
def max_of_three(x,y,z):
  return(max_of_two(x,max_of_two(y,z)))
'''
The above defined function is the basic algorithm.
The code below is extra, just to present a complete executable code.
The code below is just to input data and output the result utilising the function defined above.
'''
print("Enter three numbers:--")
num1=int(input())
num2=int(input())
num3=int(input())
print("The maximum is:",max_of_three(num1,num2,num3))
