from json import dumps
import copy

class Tree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children is not None else []

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        return self.__dict__() == other.__dict__()

    # custom deepcopy method to handle custom __dict__ method above
    def __deepcopy__(self, memo):
        new_tree = self.__class__(self.label)
        memo[id(self)] = new_tree
        new_tree.children = [copy.deepcopy(child, memo) for child in self.children]
        return new_tree

    def from_pov(self, from_node):

        if len(self.children) == 0:
            if self.label == from_node:
                return self
            else:
                raise ValueError('Tree could not be reoriented')

        def search_tree(tree, target, grandparent_tree=None, root_tree=None):
            if tree.label == target:
                return root_tree
            for j, list_element in enumerate(tree.children):
                parent_tree = copy.deepcopy(tree)

                # grandparent transposed as child of parent-turned-child
                if grandparent_tree == None:
                    grandparent_tree = copy.deepcopy(parent_tree)
                if grandparent_tree != parent_tree:
                    parent_tree.children.append(grandparent_tree)

                # target as root tree, delete target branch
                root_tree = copy.deepcopy(list_element)
                del parent_tree.children[j]

                # parent tree transposed as child
                root_tree.children.append(parent_tree)

                recursive_search_results = search_tree(list_element, target, parent_tree, root_tree)
                if recursive_search_results:
                    return recursive_search_results

        output = search_tree(self, from_node)

        if output == None:
            raise ValueError('Tree could not be reoriented')

        return output
                
    def path_to(self, from_node, to_node):
        reoriented_tree = self.from_pov(from_node)

        def search_tree(tree, to_node, path=None):
            if path == None: path = [tree.label]
            if tree.label == to_node:
                return path
            for i, child in enumerate(tree.children):
                path += [child.label]
                results = search_tree(child, to_node, path)
                if results:
                    return results
                else:
                    path = path[:-1]

        output = search_tree(reoriented_tree, to_node)

        if output:
            return output
        else:
            raise ValueError('No path found')