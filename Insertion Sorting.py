def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key


data = []
limit=int(input("Enter Size"))
for i in range (limit):
        a=input()
        data.append(a)
print("Original list:", data)
insertion_sort(data)
print("Sorted list:", data)


# This Code is Made by Shashwat Sharma
