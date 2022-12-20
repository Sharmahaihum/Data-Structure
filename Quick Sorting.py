def quick_sort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
data= []
limit=int(input("Enter Size"))
for i in range (limit):
        a=input()
        data.append(a)
final = quick_sort(data)
print(final)  



# This Code is Made by Shashwat Sharma
