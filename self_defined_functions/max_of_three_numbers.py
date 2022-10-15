def max_of_two(x,y):
  if x>y:
    return x
  return y
def max_of_three(x,y,z):
  return(max_of_two(x,max_of_two(y,z)))
print("Enter three numbers:--")
num1=int(input())
num2=int(input())
num3=int(input())
print("The maximum is:",max_of_three(num1,num2,num3))
