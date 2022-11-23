"""
"""
class _Vehicle:
    def __init__(self, asd) -> None:
        self.asd = asd
    """
    """
    def _print(self) -> None:
        print("Hello from Parent")
    
"""
"""
class _vLarge(_Vehicle):
    def __init__(self, something) -> None:
        _Vehicle.__init__(self, something)
    """
    """
    def _print(self) -> None:
        _Vehicle._print(self)
        print("Hello from Child")
    
"""
"""
class _vMedium(_Vehicle):
    def __init__(self, something) -> None:
        _Vehicle.__init__(self, something)
    """
    """
    def _print(self) -> None:
        _Vehicle._print(self)
        print("Hello from Child")

"""
""" 
class _vSmall(_Vehicle):
    def __init__(self, something) -> None:
        _Vehicle.__init__(self, something)
    """
    """
    def _print(self) -> None:
        _Vehicle._print(self)
        print("Hello from Child")