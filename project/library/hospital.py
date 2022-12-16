""" Buildings
  A
 |--|
 |A5|           C
 |A4|    B     |--|
 |A3|   |--|   |C3|
 |A2| - |B2| - |C2|
 |A1| - |B1| - |C1|
 |A0| - |B0| - |C0|
"""

import copy

class Floor:
    __Department: str
    __AssignedMedics: int
    __Supply: any
    
    def __init__(self, Department: str, AssignedMedics: int):
        self.__AssignedMedics = AssignedMedics
        self.__Department = Department
        
    """ Getters and Setters """
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
    __Coordinates: tuple[float, float]
    __Building: dict[str, Floor, list[str, int]]
    
    def __init__(self, Name: str, Street: str, Phone: str, Coordinates: tuple[float, float]):
        self.__Name = Name
        self.__Street = Street
        self.__Phone = Phone
        self.__Coordinates = Coordinates

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
    def Coordinates(self) -> tuple[float, float]:
        return self._Coordinates
    
    @Coordinates.setter
    def Coordinates(self, Coordinates: tuple[float, float]) -> None:
        self.__Coordinates = Coordinates

    @property
    def Building(self) -> dict[str, Floor, list[str, int]]:
        return self.__Building
    
    @Building.setter
    def Building(self, _JSON: any) -> None:
        _coordinates: tuple[float, float] = (float(_JSON["coordinates"]["x"]), float(_JSON["coordinates"]["y"]))
        _Hospital: Hospital = Hospital(_JSON["name"], _JSON["street"],_JSON["phone"], _coordinates )

        for _Block in _JSON["buildings"]:
            for _Floor in _Block["floors"]:
                _idFloor: str = _Block["block"] + str(_Floor["floor"])

                if _idFloor not in self.__Building:
                    self.__Building[_idFloor] = [ ]

                    for _connected in _Floor["connected_to"]:
                        _idConnected: str = _connected["block"] + str(_connected["floor"])
                        self.__Building[_idFloor].append({ _idConnected, int(_connected["cost"]) })
