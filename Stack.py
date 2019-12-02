from typing import List, Any


class Stack():
    items: List[Any]

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []


if __name__ == '__main__':
    s = Stack()
    s.push('A')
    s.push('B')
    s.push('C')
    print(s.get_stack())
    print(s.pop())
    print(s.get_stack())
    print(s.is_empty())
    print(s.get_stack())
    s.pop()
    print(s.get_stack())
    s.pop()
    print(s.get_stack())
    print(s.pop())
    print(s.get_stack())
    s.push('A')
    s.push('B')
    s.push('C')
    s.push('D')
    print(s.get_stack())
    