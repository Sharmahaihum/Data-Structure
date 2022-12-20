class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        # Insert a new node at the beginning of the list
        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data):
        # Insert a new node at the end of the list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_node(self, data):
        # Delete the first node with the given data
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def find_node(self, data):
        # Find the first node with the given data and return it, or return None if not found
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def print_list(self):
        # Print the data in each node of the list
        current = self.head
        while current:
            print(current.data)
            current = current.next


def print_menu():
    print('1. Insert at front')
    print('2. Insert at end')
    print('3. Delete node')
    print('4. Find node')
    print('5. Print list')
    print('6. Quit')
    print()


linked_list = LinkedList()

while True:
    print_menu()
    choice = int(input('Enter your choice: '))

    if choice == 1:
        data = input('Enter data to insert: ')
        linked_list.insert_at_front(data)
    elif choice == 2:
        data = input('Enter data to insert: ')
        linked_list.insert_at_end(data)
    elif choice == 3:
        data = input('Enter data to delete: ')
        linked_list.delete_node(data)
    elif choice == 4:
        data = input('Enter data to find: ')
        node = linked_list.find_node(data)
        if node:
            print('Node found:', node.data)
        else:
            print('Node not found')
    elif choice == 5:
        linked_list.print_list()
    elif choice == 6:
        break
    else:
        print('Invalid choice. Enter a number between 1 and 6.')
    print()

    
    
    
    
    # This Code is Made by Shashwat Sharma
