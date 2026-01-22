class Zipper:
    def __init__(self, tree, up = None):
        self.tree = tree
        self.left_ = tree['left']
        self.right_ = tree['right']
        self.up_ = up
        self.value_ = tree['value']
        
    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def value(self):
        return self.value_

    def set_value(self, value):
        self.tree['value'] = value
        return Zipper(self.tree, self.up_)

    def left(self):
        if self.left_ != None:
            return Zipper(self.left_, self)

    def set_left(self, value):
        self.tree['left'] = value
        return Zipper(self.tree, self.up_)

    def right(self):
        if self.right_ != None:
            return Zipper(self.right_, self)

    def set_right(self, value):
        self.tree['right'] = value
        return Zipper(self.tree, self.up_)

    def up(self):
        if self.up_ != None:
            return self.up_

    def to_tree(self):
        branch = self
        while branch.up_ != None:
            branch = branch.up_

        return branch.tree
