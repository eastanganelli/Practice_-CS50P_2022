class Node:
    _Value: any
    _Next: any
    
    def __init__(self, _Value: any) -> None:
        self._Value = _Value
        self._Next = None
        
class Stack:
    _Head: any
    _Size: int
    
    def __init__(self) -> None:
        self._Head = None
        self._Size = 0
        
    def _Size(self) -> int:
        return self._Size
    
    def isEmpty(self) -> bool:
        return self._Size == 0
    
    def push(self, _Value: any):
        node: Node = Node(_Value)
        node._Next = self._Head
        self._Head = node
        self._Size += 1
    
    def pop(self) -> Node:
        node: Node = self._Head
        self._Head = node._Next
        node._Next = None
        self._Size -= 1
        return node