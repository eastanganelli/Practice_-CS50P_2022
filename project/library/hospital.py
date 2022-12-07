""" Buildings
  A
 ____
 |A5|        C
 |A4|   B  ____
 |A3| ____ |C3|
 |A2|-|B2|-|C2|
 |A1|-|B1|-|C1|
 |A0|-|B0|-|C0|
"""

class Floor:
    _Department: str
    _AssignedMedics: int
    _Supply: any
    
    def __init__(self, _Department: str, _AssignedMedics: int):
        self._AssignedMedics = _AssignedMedics
        self._Department = _Department
        
    """
    Getters and Setters    
    """
    """ @property
    def _Department(self) -> str:
        return self._Department
    
    @_Department.setter
    def _Department(self, _Department: str) -> None:
        if _Department.count > 0:
            self._Department = _Department
            
    @property
    def _AssignedMedics(self) -> int:
        return self._AssignedMedics
    
    @_AssignedMedics.setter
    def _AssignedMedics(self, _AssignedMedics: int) -> None:
        if _AssignedMedics.count > 0:
            self._AssignedMedics = _AssignedMedics """

class Building:
    _Building: str
    _Floors: list[Floor]
    
    def __init__(self, _Floors: list[Floor]):
        self._Floors = _Floors
        
    """
    Getters and Setters
    """
    """ @property
    def _Building(self) -> str:
        return self._Building
    
    @_Building.setter
    def _Building(self, _Building: str) -> None:
        if _Building.count > 0:
            self._Building = _Building
    
    @property
    def _Floors(self) -> list[Floor]:
        return self._Floors

    @_Floors.setter
    def _Floors(self, _Floors: list[Floor]) -> None:
        if len(_Floors) > 0:
            self._Floors = _Floors """
    
    def CountFloors(self) -> int:
        return len(self._Floors)

class Hospital:
    _Name:   str
    _Street: str
    _Phone:  str
    _Coordinates: tuple[int, int]
    _Specialization: str
    _Building: dict[str, Building]
    
    def __init__(self, _Name: str, _Street: str, _Phone: str, _Coordinates: tuple[int, int], _Specialization: str):
        self._Name = _Name
        self._Street = _Street
        self._Phone = _Street
        self._Specialization = _Specialization
        self._Coordinates = _Coordinates
    
    """
    Getters and Setters    
    """
    @property
    def _Name(self):
        return self._Name
    
    @_Name.setter
    def _Name(self, _Name: str):
        if _Name.count > 0:
            self._Name = _Name
            
    @property
    def _Street(self):
        return self._Street
    
    @_Street.setter
    def _Street(self, _Street: str):
        if _Street.count > 0:
            self._Street = _Street
    
    @property
    def _Phone(self):
        return self._Phone
    
    @_Phone.setter
    def _Phone(self, _Phone: str):
        if _Phone.count > 0:
            self._Phone = _Phone
            
    @property
    def _Specialization(self):
        return self._Specialization
    
    @_Specialization.setter
    def _Specialization(self, _Specialization: str):
        if _Specialization.count > 0:
            self._Specialization = _Specialization
    
    @property
    def _Coordinates(self):
        return self._Coordinates
    
    @_Coordinates.setter
    def _Coordinates(self, _Coordinates: tuple[int, int]):
        if _Coordinates.count > 0:
            self._Coordinates = _Coordinates
