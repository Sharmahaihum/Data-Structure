n=int(input("Enter total number of Elements"))
l1=[]
for i in range(n):
    a=int(input("Enter value"))
    l1.append(a)
b=int(input("Enter value to be searched"))
for i in range(n):
    if b==l1[i]:
        print("found")
        break
    else:
        print("not found")
        break