from pathlib import Path

class LinkedNode:
    'Связный список с ссылками на обратный и следующий элемент'
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None
        
# Класс для стека
class Stack:
    def __init__(self):
        self.head = LinkedNode()
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, value):
        if self.size > 0:
            node = LinkedNode(value)
            node.right = self.head
            self.head = node
        else:
            self.head.value = value
        self.size += 1
      
    def pop(self):
        if self.is_empty():
            raise Exception("Popping from an empty stack")
        remove = self.head
        if self.size > 1:
            self.head = remove.right
        self.size -= 1
        return remove.value
    
    def peek(self):
        if self.is_empty():
            raise Exception("Popping from an empty stack")
        return self.head.value
    
    def __len__(self):
        return self.size

    def reverse(self):
        current = self.head
        prev = None
        next = None
    
        while current is not None:
            next = current.right
            current.right = prev
            prev = current
            current = next

        self.head = prev