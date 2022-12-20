def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            print("Data found at:",i)
    

def main():
    data = []
    limit=int(input("Enter size of list"))
    for i in range (limit):
        a=input()
        data.append(a)
    target = input("Enter a target value: ")
    index = linear_search(data, target)
        

if __name__ == '__main__':
    main()

    
    
    # This Code is Made by Shashwat Sharma
