'''

A Binary Search Tree (BST) is a special type of binary tree where each node follows this rule:
Left child < Parent node < Right child

This property makes searching, inserting, and deleting data very fast and efficient (on average, in O(log n) time).

'''

# Example usage
root = Node(50)
insert(root, 30)
insert(root, 70)
insert(root, 20)
insert(root, 40)
insert(root, 60)
insert(root, 80)

print("Inorder Traversal of BST:")
inorder(root)