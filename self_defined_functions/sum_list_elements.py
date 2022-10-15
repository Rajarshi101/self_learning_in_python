def sum_list_elements(list1):
  total = 0
  for i in list1:
    total += i
  return total
'''
The above defined function is the basic algorithm.
The code below is extra, just to present a complete executable code.
The code below is just to input data and output the result utilising the function defined above.
'''
lst=[]
size=int(input("Enter the size of list: "))
print("Enter the elements of the list:--")
for i in range(size):
  x=int(input())
  lst.append(x)
print("The list is:",lst)
print("The sum of all elements in the list is:",sum_list_elements(lst))
