import numpy as np
import numpy.random as rand
import time

array = np.sort(rand.randint(0,100,10))


class BSTNode:
    def __init__(self, value: float | int = None, index: int | set[int] = None):
        self.left = None
        self.right = None
        if value is None or index is None: raise TypeError
        self.value: float | int = value
        self.index: set[int]
        if type(index) is set:
            self.index = index
        elif type(index) is int:
            self.index = {index}

    def insert(self, other):
        if self == other:
            self.index.update(other.index)
            return
        if other < self:
            if self.left is not None:
                self.left.insert(other)
                return
            self.left = other
        else:
            if self.right is not None:
                self.right.insert(other)
                return
            self.right = other

    def __eq__(self, other):
        if type(other) is BSTNode:
            return self.value == other.value
        return False

    def __lt__(self, other):
        if type(other) is BSTNode:
            return self.value < other.value
        return False

    def __gt__(self, other):
        if type(other) is BSTNode:
            return self.value > other.value
        return False

    def search(self, other):
        if self == other:
            return self
        if self.right is not None and other < self.right:
            return self.right.search(other)
        if self.left is not None and other > self.left:
            return self.left.search(other)
        return None
        

    


class BST:
    def __init__(self, massiv: list[int | float] = None):
        self.massiv = sorted(massiv) if massiv is not None else []
        self.middle = len(self.massiv) // 2
        self.tree = BSTNode(self.massiv[self.middle], self.middle)
        for index, element in enumerate(self.massiv[self.middle:]):
            self.tree.insert(BSTNode(element, index))
        for index, element in enumerate(self.massiv[0:self.middle:-1]):
            self.tree.insert(BSTNode(element, index))

    def search(self, value: int | float):
        search_result = self.tree.search(BSTNode(value, 0))
        if search_result is not None:
            return search_result.index
        return None


bst = BST(array)
print(bst.search(array[4]))