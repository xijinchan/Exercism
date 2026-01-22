class TreeNode:
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        
        def add_node(top_node, data):
            current_node = top_node
            next_data = data[0]
            
            while current_node != None:
                if next_data <= current_node.data:
                    if current_node.left is None:
                        current_node.left = TreeNode(next_data, parent=current_node)
                        break
                    else:
                        current_node = current_node.left
                if next_data > current_node.data:
                    if current_node.right is None:
                        current_node.right = TreeNode(next_data, parent=current_node)
                        break
                    else:
                        current_node = current_node.right

        top_node = TreeNode(tree_data[0])
        
        for k in range(len(tree_data[:-1])):
            add_node(top_node, tree_data[k+1])

        self.tree = top_node

    def data(self):
        return self.tree

    def sorted_data(self):
        sorted = []

        def ordered_traverse(root, sorted):
            if root != None:
                ordered_traverse(root.left, sorted)
                sorted.append(root.data)
                ordered_traverse(root.right, sorted)
                return sorted

        return ordered_traverse(self.tree, sorted)
        
                
        
                
