def selection_sort(data):
    for i in range(len(data)-1):
        min_index = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]


data = []
limit=int(input("Enter Size"))
for i in range (limit):
        a=input()
        data.append(a)
print("Original list:", data)
selection_sort(data)
print("Sorted list:", data)


