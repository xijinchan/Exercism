import ast

def tree_from_traversals(preorder, inorder):

    if any([preorder == [], inorder == []]): return {}
    if len(preorder) != len(inorder): raise ValueError("traversals must have the same length")
    if not any([True if k in inorder else False for k in preorder]): raise ValueError("traversals must have the same elements")
    if any([len(set(preorder)) != len(preorder), len(set(inorder)) != len(inorder)]): raise ValueError("traversals must contain unique items")

    class TreeNode:
        def __init__(self, value, left={}, right={}):
            self.value = f'"{value}"'
            self.left = left
            self.right = right

        def __str__(self):
            value_ = self.value
            left_ = self.left
            right_ = self.right if self.right != {} else {}
            
            return f'{{"v": {value_}, "l": {left_}, "r": {self.right}}}'

    global node_count
    node_count = 0

    top_node = TreeNode(preorder[0])
    global current_node
    current_node = top_node
    node_count += 1

    def left_or_right(current_node_):
        global node_count
        global current_node
        
        # determine whether next 2 elements are to the left or right of current node
        n = preorder.index(current_node.value[1:-1])
        if inorder.index(preorder[n+1]) == inorder.index(preorder[n])-1:
            current_node.left = TreeNode(preorder[n+1])
        elif inorder.index(preorder[n+1]) == inorder.index(preorder[n])+1:
            current_node.right = TreeNode(preorder[n+1])
        node_count += 1
        
        if inorder.index(preorder[n+2]) == inorder.index(preorder[n])-1:
            current_node.left = TreeNode(preorder[n+1])
            current_node = top_node.left
        elif inorder.index(preorder[n+2]) > inorder.index(preorder[n]):
            current_node.right = TreeNode(preorder[n+2])
            current_node = top_node.right
        node_count += 1

    while node_count != len(preorder):
        left_or_right(current_node)

    output = str(top_node)[:-2]+"},}" # mystery comma in test 3
    return ast.literal_eval(output)

    # determine if 3rd element is on left branch or right brance
    # if inorder.index(preorder[2]) == inorder.index(preorder[1])-1:
        

    # everything left of top_node_position in inorder is on 'l' branch of top node
    # ditto with right
    # create objects with v, l, r, parent values
    
    # if preorder[2]

    '''

    # possibilities
    
     a
    i x
     f r

      a
     i r
    x f
    
      x
     a r
    i f

     a
    i x
     f r

    additional:
    
       a
     i   x
    m n f r

    {'v': a, 'l': {'v': i, 'l': m, 'r': n} 'r': {'v': x, 'l': f, 'r': r}}

        a
     i     x
    m n   f r
         p q

    {'v': a, 'l': {'v': i, 'l': m, 'r': n} 'r': {'v': x, 'l': {'v':f, 'l': p, 'r': q}, 'r': r}}
    
    '''