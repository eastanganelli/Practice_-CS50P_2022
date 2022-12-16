class Supply:
    _ProductName: str
    _Price: float
    _Count: int
    
    def __init__(self) -> None:
        pass
    
class ProcedureEquipement(Supply):
    def __init__(self) -> None:
        super().__init__()
    
class EmergencyEquipment(Supply):
    def __init__(self) -> None:
        super().__init__()
    
class ProtectiveEquipement(Supply):
    def __init__(self) -> None:
        super().__init__()

class BasicDiagnosticEquipment(Supply):
    def __init__(self) -> None:
        super().__init__()
