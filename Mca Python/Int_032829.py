list1 = []
list2 = []
m = int(input("Enter the limit of list1:"))
print("Enter the elements")
for i in range(0,m):
          value = int(input())
          list1.append(value)
n = int(input("Enter the lit of list2:"))
print("Enter the elements")
for i in range(0,n):
          value = int(input())
          list2.append(value)
print(list1,list2)
if len(list1)==len(list2):
          print("Both List1 and List2 are of the same length")
else:
          print("Both List1 and List2 are Not of the same length")
if sum(list1) == sum(list2):
            print("The sum of both List1 and List2 are same")
else:
            print("The sum of both List1 and List2 are Not same")
list3 = [each for each in list1 if each in list2]
print("Same Members are:",list3)
      
      
