from typing import Any, List, Callable, Union



class TreeNode:
    value : Any
    children : List['TreeNode']

    def __init__(self, value : Any):
        self.value = value
        self.children = []

    def is_leaf(self)-> bool:
        if(self.children == None):
            return True
        return False

    def add(self, child: 'TreeNode')-> None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None])-> None:
        if (visit != None):
            return
        visit(self)

        for child in self.children:
            self.for_each_deep_first(visit(child))

    def for_each_level_order(self, visit: Callable[['TreeNode'], None])-> None:
        if (visit != None):
            return

        visit(self)

        fifo = self.children

        while len(fifo):
            print(fifo[0])
            fifo += fifo[0]


    def search(self, value: Any) -> Union['TreeNode', None]:
        if self.value == value:
            return self

        search_node = None
        for child in self.children:
            a = child.search(value)
            if a:
                search_node = a
        return search_node


    def print(self):
        print(self.value)
        for child in self.children:
            child.print()

class Tree:
    root: TreeNode

    def __init__(self, tree_node):
        self.root = tree_node

    def add(self, value: Any, parent_name: Any) -> None:
        nowe = self.root.search(parent_name)
        nowe.add(TreeNode(value))

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(visit)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_deep_first(visit)

    def show(self):
        pass



f = TreeNode("F")
tree = Tree(f)
b = TreeNode("B")
f.add(b)
a = TreeNode("A")
b.add(a)
d = TreeNode("D")
b.add(d)
c = TreeNode("C")
d.add(c)
e = TreeNode("E")
d.add(e)
g = TreeNode("G")
f.add(g)
i = TreeNode("I")
g.add(i)
h = TreeNode("H")
i.add(h)



TreeNode.print(f)



#
# tree.show()