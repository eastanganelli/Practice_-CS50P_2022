import sys
import json
from simple_term_menu import TerminalMenu

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
    MyHospital: Hospital = None
    
    try:
        path: str = base_path + file_name
        with open(path, "r") as file:
            myJson = json.load(file)
            MyHospital = Hospital(myJson["name"], myJson["street"], myJson["phone"])            

    except FileNotFoundError:
        sys.exit("File not Found, program can´t continue...")

        _name  : str = input("Hospital name >> ")
        _street: str = input("Street >> ")
        _phone : str = input("Phone number >> ")

        MyHospital = Hospital(_name, _street, _phone)

    return Hospital

def menu():
    options = ["entry 1", "entry 2", "entry 3", "exit"]
    Terminal_menu = TerminalMenu(options)
    menu_entry_index = Terminal_menu.show()
    

if __name__ == "__main__":
    main()
