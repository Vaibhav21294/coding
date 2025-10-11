# Define a Tree Node
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    # Add child node
    def add_child(self, child_node):
        self.children.append(child_node)

    # Display tree recursively
    def display(self, level=0):
        print(" " * level * 2 + f"- {self.data}")
        for child in self.children:
            child.display(level + 1)

# Create a root node
root = Node("Electronics")

# Create child nodes
laptop = Node("Laptop")
phone = Node("Phone")
tv = Node("TV")

# Add children to root
root.add_child(laptop)
root.add_child(phone)
root.add_child(tv)

# Add sub-children
laptop.add_child(Node("MacBook"))
laptop.add_child(Node("Dell"))
phone.add_child(Node("iPhone"))
phone.add_child(Node("Samsung"))

# Display the tree
root.display()
