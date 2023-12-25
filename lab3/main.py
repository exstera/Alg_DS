class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if self.left is None:
            self.left = TreeNode(key)
        elif self.left and self.right is None:
            self.right = TreeNode(key)
        else:
            raise ValueError("Node already has two children.")

def parse_bracket_notation(s):
    stack = []
    current_node = None
    digit_buffer = []
    for char in s:
        if char == '(':
            if current_node is not None:
                stack.append(current_node)
            current_node = TreeNode(None)
        elif char.isdigit():
            digit_buffer.append(char)
        elif char in [' ', ')']:
            if digit_buffer:
                current_node.key = int(''.join(digit_buffer))
                digit_buffer = []
            if char == ')' and stack:
                child_node = current_node
                current_node = stack.pop()
                if current_node.left is None:
                    current_node.left = child_node
                elif current_node.right is None:
                    current_node.right = child_node
                else:
                    raise ValueError("Node already has two children.")
    if stack or digit_buffer:
        raise ValueError("The input is not a valid binary tree.")

    return current_node  # Root node

def depth_first_traversal_iterative(root):
    if root is None:
        return []
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.key)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# Example usage:
tree_str = "(8 (9 (5)) (1))"
try:
    root = parse_bracket_notation(tree_str)
    print("Depth-First Traversal Iterative:")
    depth_first_traversal_iterative(root)
except ValueError as e:
    print(f"Error parsing tree: {e}")



class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def height(node):
    if not node:
        return 0
    return node.height

def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1

def balance_factor(node):
    return height(node.left) - height(node.right)

def rotate_left(z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    update_height(z)
    update_height(y)
    return y

def rotate_right(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    update_height(y)
    update_height(x)
    return x

def balance(node):
    if balance_factor(node) > 1:
        if balance_factor(node.left) < 0:
            node.left = rotate_left(node.left)
        return rotate_right(node)
    if balance_factor(node) < -1:
        if balance_factor(node.right) > 0:
            node.right = rotate_right(node.right)
        return rotate_left(node)
    return node

def insert_avl(root, key):
    if not root:
        return AVLNode(key)
    elif key < root.key:
        root.left = insert_avl(root.left, key)
    else:
        root.right = insert_avl(root.right, key)
    update_height(root)
    return balance(root)

def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.key)
        in_order_traversal(node.right)

# Создание АВЛ и вывод отсортированных значений
avl_root = None
values_to_insert = [10, 20, 30, 40, 50, 25]

for value in values_to_insert:
    avl_root = insert_avl(avl_root, value)

print("\nIn-order Traversal of AVL Tree:")
in_order_traversal(avl_root)
