def max_of_two(x,y):
  if x>y:
    return x
  return y
'''
The above defined function is the basic algorithm.
The code below is extra, just to present a complete executable code.
The code below is just to input data and output the result utilising the function defined above.
'''
print("Enter two numbers:--")
num1=int(input())
num2=int(input())
print("The maximum is:",max_of_two(num1,num2))
