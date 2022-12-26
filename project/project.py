import sys

from library.supply   import Supply  , read_supply_list, prices_to_table
from library.hospital import Hospital, read_hopsital

base_path: str = ".\\data\\"

def main() -> None:
    MyHospital: Hospital = init_hospital()
    SupplyPriceList: list[Supply] = init_supply()
    ...
    
def init_supply(file_name: str = "pricelist.csv") -> list[Supply]:
    try:
        path: str = base_path + file_name
        with open(path, "r") as file:
            SupplyPriceList = read_supply_list(file)
            prices_to_table(SupplyPriceList)
    except FileNotFoundError:
        sys.exit("File not Found, program can´t continue...")
    else:
        return SupplyPriceList

def init_hospital(file_name: str = "hospital") -> Hospital:
    _name  : str = input("Hospital name >> ")
    _street: str = input("Street >> ")
    _phone : str = input("Phone number >> ")

    MyHospital: Hospital = Hospital(_name, _street, _phone)
    
    try:
        path: str = base_path + file_name
        
    except FileNotFoundError:
        sys.exit("File not Found, program can´t continue...")

    return Hospital

if __name__ == "__main__":
    main()
