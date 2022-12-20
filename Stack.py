class Stack:
    def __init__(self):
        # Initialize an empty stack
        self.items = []

    def push(self, item):
        # Add an item to the top of the stack
        self.items.append(item)

    def pop(self):
        # Remove and return the item at the top of the stack
        return self.items.pop()

    def peek(self):
        # Return the item at the top of the stack without removing it
        return self.items[-1]

    def is_empty(self):
        # Return True if the stack is empty, False otherwise
        return not self.items
    def display(self):
        # Print the items in the stack
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
