def binary_search(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main():
    data = []
    limit=int(input("Enter size of list"))
    for i in range (limit):
        a=input()
        data.append(a)
    target = input("Enter a target value: ")
    index = binary_search(data, target)
    if index == -1:
        print("Value not found")
    else:
        print("Value found at index", index)

if __name__ == '__main__':
    main()

    
    
    
   
    
# This Code is Made by Shashwat Sharma
