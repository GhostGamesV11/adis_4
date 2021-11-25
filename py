from typing import Any, List, Callable, Union
from anytree import Node, RenderTree
from anytree.exporter import DotExporter
 
 
class TreeNode:
    value: Any
    children: List['TreeNode']
 
    def __init__(self, value):
        self.value = value
        self.children = []
 
    def is_leaf(self):
        if not len(self.children):
            return False
        return True
 
    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)
 
    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        if visit:
            return
 
        visit(self)
 
        for child in self.children:
            self.for_each_deep_first(visit(child))
 
    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        if visit:
            return
 
        visit(self)
 
        fifo = self.children
 
        while len(fifo):
            print(fifo[0])
            fifo += fifo[0]
 
            del fifo[0]
 
    def search(self, value: Any) -> Union['TreeNode', None]:
        if self.value == value:
            return self
 
        search_node = None
        for child in self.children:
            output = child.search(value)
 
            if output:
                search_node = output
 
        return search_node
 
    def __str__(self):
        return self.value
 
class Tree:
    root: TreeNode
 
    def __init__(self, tree_node):
        self.root = tree_node
 
    def add(self, value: Any, parent_name: Any) -> None:
        node = self.root.search(parent_name)
 
        node.add(TreeNode(value))
 
    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(visit)
 
    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_deep_first(visit)
 
    def show(self):
        root = Node(self.root.value)
        a = Node("OW", root)
 
        DotExporter(root).to_picture("tree.png")
 
 
# f = TreeNode("F")
# tree = Tree(f)
# b = TreeNode("B")
# f.add(b)
# a = TreeNode("A")
# b.add(a)
# d = TreeNode("D")
# b.add(d)
# c = TreeNode("C")
# d.add(c)
# e = TreeNode("E")
# d.add(e)
#
# tree.show()
#
# def test(k):
#     print(k)
#
# print(f.for_each_level_order(test(e)))
