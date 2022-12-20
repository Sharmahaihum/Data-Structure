class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right

    def search(self, data):
        current = self.root
        while current is not None:
            if current.data == data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def delete(self, data):
        # find the node to delete
        current = self.root
        parent = None
        while current is not None and current.data != data:
            parent = current
            if data < current.data:
                current = current.left
            else:
                current = current.right
        if current is None:
            return False

        # case 1: the node to delete has no children
        if current.left is None and current.right is None:
            if parent is None:
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None
        # case 2: the node to delete has one child
        elif current.right is None:
            if parent is None:
                self.root = current.left
            elif parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left
        elif current.left is None:
            if parent is None:
                self.root = current.right
            elif parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right
        # case 3: the node to delete has two children
        else:
            successor = current.right
            while successor.left is not None:
                successor = successor.left
            current.data = successor.data
            # delete the successor node
            self.delete(successor.data)

        return True
    
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=' ')

    def preorder(self, node):
        if node is not None:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

# menu-driven interface
def main():
    tree = BinaryTree()
    while True:
        print("1. Insert a value")
        print("2. Search for a value")
        print("3. Delete a value")
        print("4. Inorder traversal")
        print("5. Postorder traversal")
        print("6. Preorder traversal")
        print("7. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            value = int(input("Enter the value to insert: "))
            tree.insert(value)
        elif choice ==2:
            value = int(input("Enter the value to search: "))
            if tree.search(value)==False:
                print("Element not present")
            else: 
                print("Element present")
            
        elif choice ==3:
            value = int(input("Enter the value which you want to delete: "))
            tree.delete(value)
        elif choice == 4:
            tree.inorder(tree.root)
            print()
        elif choice == 5:
            tree.postorder(tree.root)
            print()
        elif choice == 6:
            tree.preorder(tree.root)
            print()
        elif choice==7:
            break;
if __name__ == '__main__':
    main()


# This Code is Made by Shashwat Sharma
