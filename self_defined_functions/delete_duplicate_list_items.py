def unique_list(list1):
  list2=[]
  for i in list1:
    if i not in list2:
      list2.append(i)
  return list2
lst=[]
size=int(input("Enter the size of the list: "))
print("Enter the elements of the list:--")
for i in range(size):
  x=input()
  lst.append(x)
print("The given list is:",lst)
print("List after duplicate item deletion:",unique_list(lst))
