def bubble_sort(data):
    for i in range(len(data)-1):
        for j in range(len(data)-1-i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]


data = []
limit=int(input("Enter size of list"))
for i in range (limit):
        a=input()
        data.append(a)
while True:
    print("Original list:", data)
    bubble_sort(data)
    print("Sorted list:", data)
    again = input("Sort again? (y/n) ")
    if again != 'y':
        break


