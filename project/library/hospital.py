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

class Building:
    __Floors: list[Floor]
    
    def __init__(self, Floors: list[Floor]):
        self.__Floors = Floors
        
    """
    Getters and Setters
    """
    @property
    def Floors(self) -> list[Floor]:
        return self.__Floors

    @Floors.setter
    def Floors(self, Floors: list[Floor]) -> None:
        if len(Floors) > 0:
            self.__Floors = Floors
    
    def Floors(self) -> int:
        return len(self._Floors)

class Hospital:
    __Name:   str
    __Street: str
    __Phone:  str
    __Coordinates: tuple[int, int]
    __Specialization: str
    __Building: dict[str, Building]
    
    def __init__(self, Name: str, Street: str, Phone: str, Coordinates: tuple[int, int], Specialization: str):
        self.__Name = Name
        self.__Street = Street
        self.__Phone = Phone
        self.__Specialization = Specialization
        self.__Coordinates = Coordinates
    
    """
    Getters and Setters    
    """
    @property
    def Name(self):
        return self.__Name
    
    @Name.setter
    def Name(self, Name: str):
        if len(Name) > 0:
            self.__Name = Name
            
    @property
    def Street(self):
        return self.__Street
    
    @Street.setter
    def Street(self, Street: str):
        if len(Street) > 0:
            self.__Street = Street
    
    @property
    def Phone(self):
        return self.__Phone
    
    @Phone.setter
    def Phone(self, Phone: str):
        if len(Phone) > 0:
            self.__Phone = Phone
            
    @property
    def Specialization(self):
        return self.__Specialization
    
    @Specialization.setter
    def Specialization(self, Specialization: str):
        if len(Specialization) > 0:
            self.__Specialization = Specialization
    
    @property
    def Coordinates(self):
        return self._Coordinates
    
    @Coordinates.setter
    def Coordinates(self, Coordinates: tuple[int, int]):
        self.__Coordinates = Coordinates
