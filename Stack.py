class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return not self.items
    def display(self):
        for item in self.items:
            print(item)


def print_menu():
    print('1. Push an item onto the stack')
    print('2. Pop an item from the stack')
    print('3. Peek at the top item on the stack')
    print('4. Check if the stack is empty')
    print('5. Quit')
    print('6.Display')
    print()


stack = Stack()

while True:
    print_menu()
    choice = int(input('Enter your choice: '))

    if choice == 1:
        item = input('Enter an item to push: ')
        stack.push(item)
    elif choice == 2:
        if stack.is_empty():
            print('The stack is empty.')
        else:
            print('Popped', stack.pop())
    elif choice == 3:
        if stack.is_empty():
            print('The stack is empty.')
        else:
            print('Peeked', stack.peek())
    elif choice == 4:
        if stack.is_empty():
            print('The stack is empty.')
        else:
            print('The stack is not empty.')
    elif choice == 5:
        break
    elif choice==6:
        print("Stack contains:",stack.display())
    else:
        print('Invalid choice. Enter a number between 1 and 6.')
    print()

    
    
    # This Code is Made by Shashwat Sharma
