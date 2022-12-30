import regex

phone_pattern: str = "^\s*(?:\+?(\d{1,3}))?([-. (]*(\d{3})[-. )]*)?((\d{3})[-. ]*(\d{2,4})(?:[-.x ]*(\d+))?)\s*$"

class Department:
    
    def __init__(self) -> None:
        self.__Supplies = dict()

    @property
    def Supplies(self) -> dict[str, int]:
        return self.__Supplies

    @Supplies.setter
    def Supplies(self, Supplies: dict[str, int]) -> None:
        self.__Supplies = Supplies

    def SuppliesStatus(self) -> list[str, int]:
        LowSupplies: list[str, int] = list()
        
        for supply in self.__Supplies.keys():
            if self.__Supplies[supply] < 6:
                pass
    
    def __str__(self) -> str:
        SuppliesData: str = None

        for supply_ in self.__Supplies.keys():
            SuppliesData += f"|-\t\t|-{supply_} : {self.__Supplies[supply_]}"

        return SuppliesData

class Hospital:

    def __init__(self, Name: str, Street: str, Phone: str) -> None:
        if not Name:
            raise ValueError("Invalid Name")
        
        if not Street:
            raise ValueError("Invalid Street")

        if not Phone and regex.match(phone_pattern, Phone):
            raise ValueError("Invalid Phone Number\nie: +54 911 67208901")

        self.__Name   = Name
        self.__Phone  = Phone
        self.__Street = Street
        self.__Departments = { }

    def __str__(self) -> str:
        txt: str = f"{self.__Name}\nStreet: {self.__Street}\nPhone: {self.__Phone}\n\nDeparments:\n"
        for department in self.__Departments.keys():
            txt += f"\n|-{department}:\n{self.__Departments[department]}"
        
        return txt

    @staticmethod
    def read_hopsital(HospitalFile: any) -> any:
        priceList: dict[str, Department] = dict()

        dummy: str = None

        for line in HospitalFile:
            if dummy is None:
                dummy = line
            else:
                ...