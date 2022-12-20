class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head
            self.head = new_node

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            if self.head == self.head.next:
                self.head = None
            else:
                current_node.next = self.head.next
                self.head = self.head.next
        else:
            current_node = self.head
            while current_node.next != self.head:
                if current_node.next.data == data:
                    current_node.next = current_node.next.next
                    break
                current_node = current_node.next

    def display(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
            if current_node == self.head:
                break
        print(elements)

c_list = CircularLinkedList()

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
        c_list.append(data)
    elif choice == 2:
        data = input("Enter the element to prepend: ")
        c_list.prepend(data)
    elif choice == 3:
        data = input("Enter the element to delete: ")
        c_list.delete(data)
    elif choice == 4:
        c_list.display()
    elif choice == 5:
        break
   
