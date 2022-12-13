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
    __Department: str
    __AssignedMedics: int
    __Supply: any
    
    def __init__(self, Department: str, AssignedMedics: int):
        self.__AssignedMedics = AssignedMedics
        self.__Department = Department
        
    """
    Getters and Setters    
    """
    @property
    def Department(self) -> str:
        return self.__Department
    
    @Department.setter
    def Department(self, Department: str) -> None:
        if len(Department) > 0:
            self.__Department = Department
            
    @property
    def AssignedMedics(self) -> int:
        return self.__AssignedMedics
    
    @AssignedMedics.setter
    def AssignedMedics(self, AssignedMedics: int) -> None:
        if AssignedMedics > 0:
            self.__AssignedMedics = AssignedMedics

class Hospital:
    __Name:   str
    __Street: str
    __Phone:  str
    __Coordinates: tuple[int, int]
    __Building: dict[str, Floor, list(str, int)]
    
    def __init__(self, Name: str, Street: str, Phone: str, Coordinates: tuple[int, int]):
        self.__Name = Name
        self.__Street = Street
        self.__Phone = Phone
        self.__Coordinates = Coordinates
    
    def addFloor(self, fromFloor: str, toFloor: str, cost: int) -> None:
        if fromFloor not in self.__Building:
            self.__Building[fromFloor] = []
            
        if toFloor not in self.__Building:
            self.__Building[toFloor] = []
            
        self.__Building[fromFloor].append(( toFloor, int(cost) ))
    
    
    def AddToGraph(self, ):
        
    
    def RemoveFromGraph():
        pass
    
    """
    Getters and Setters    
    """
    @property
    def Name(self) -> str:
        return self.__Name
    
    @Name.setter
    def Name(self, Name: str) -> None:
        if len(Name) > 0:
            self.__Name = Name
            
    @property
    def Street(self) -> str:
        return self.__Street
    
    @Street.setter
    def Street(self, Street: str) -> None:
        if len(Street) > 0:
            self.__Street = Street
    
    @property
    def Phone(self) -> str:
        return self.__Phone
    
    @Phone.setter
    def Phone(self, Phone: str) -> None:
        if len(Phone) > 0:
            self.__Phone = Phone
    
    @property
    def Coordinates(self) -> tuple[int, int]:
        return self._Coordinates
    
    @Coordinates.setter
    def Coordinates(self, Coordinates: tuple[int, int]) -> None:
        self.__Coordinates = Coordinates
        
    @property
    def Building(self) -> dict[str, Floor, list(str, int)]:
        return self.__Building
        
    @Building.setter
    def Building(self, Building: dict[str, Floor, list[str, int]]) -> None:
        self.__Building = Building
        
    @Building.__str__
    def Building(self) -> str:
        return "None Text"
