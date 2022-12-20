class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    self.head = current_node.next
                    current_node.next.prev = None
                break
            current_node = current_node.next

    def display(self):
        elements = []
        current_node = self.head
        while current_node is not None:
            elements.append(current_node.data)
            current_node = current_node.next
        print(elements)

dl_list = DoubleLinkedList()

while True:
    print("Menu:")
    print("1. Append an element")
    print("2. Prepend an element")
    print("3. Delete an element")
    print("4. Display the list")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = input("Enter the element to append: ")
        dl_list.append(data)
    elif choice == 2:
        data = input("Enter the element to prepend: ")
        dl_list.prepend(data)
    elif choice == 3:
        data = input("Enter the element to delete: ")
        dl_list.delete(data)
    elif choice == 4:
        dl_list.display()
    elif choice == 5:
        break
    else:
        print("Invalid choice")

        
        
  # This Code is Made by Shashwat Sharma
