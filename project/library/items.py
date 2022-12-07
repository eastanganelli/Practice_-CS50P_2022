class items:
    _ProductName: str
    _Price: float
    _Count: int
    
    def __init__(self) -> None:
        pass
    
class medication(items):
    _MinDose: int
    _MaxDose: int
    
    def __init__(self) -> None:
        super().__init__()
    
class instruments(items):
    def __init__(self) -> None:
        super().__init__()
    
class badge(items):
    _BadgeType: str
    
    def __init__(self) -> None:
        super().__init__()
        