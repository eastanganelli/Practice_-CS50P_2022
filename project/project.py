import signal
import readchar
import sys
import json
from os                 import name, system

from library.supply     import Supply, prices_to_table
from library.hospital   import Hospital
from library.exceptions import SupplyInStockException, SupplyInvalidException

base_path: str = ".\\data\\"
_files: dict[str, str] = {
    "pricelist": "pricelist.csv",
    "hospital": "hospital.json",
    "departments": "departments.csv"
}
options: list[str] = ["1 - Check Departments supplies", "2 - Resupply Departments", "3 - Check Supplies Prices"]

def handler(signum, frame):
    msg: str = "Ctrl-c was pressed. Do you really want to exit? y/n"
    print(msg, end="", flush=True)
    response = readchar.readchar()
    if response == "y":
        exit()

signal.signal(signal.SIGINT, handler)

MyHospital: Hospital = None
SupplyPriceList: list[Supply] = None

def main() -> None:
    """
    Load data from files into memory
    """
    MyHospital = init_hospital()
    SupplyPriceList = init_supply()

    while True:
        try:
            for val_ in options:
                print(val_)
        
            menu(input("Select option >> "))
        except EOFError:
            clear()
            pass
    
def init_supply() -> list[Supply]:
    try:
        path: str = base_path + _files["pricelist"]
        with open(path, "r") as file:
            SupplyPriceList = Supply.read_supply_list(file)
    except FileNotFoundError:
        sys.exit(f'File {_files["pricelist"]} not Found, program can´t continue...')
    else:
        return SupplyPriceList

def init_hospital() -> Hospital:
    MyHospital: Hospital = None
    path: str = None    

    """ Load Hospital information into memory """

    try:
        path = base_path + _files['hospital']
        with open(path, "r") as file:
            myJson = json.load(file)
            MyHospital = Hospital(myJson["name"], myJson["street"], myJson["phone"])            

    except FileNotFoundError:
        print(f"File {_files['hospital']} not Found...\nPlease complete the following information:")

        _name  : str = input("Hospital name >> ")
        _street: str = input("Street >> ")
        _phone : str = input("Phone number >> ")

        HospitalInfo = {
            "name":_name,
            "street":_street,
            "phone":_phone
        }

        MyHospital = Hospital(_name, _street, _phone)

        with open(path, "w") as outfile:
            json.dump(HospitalInfo, outfile)

    """ Load Departments into memory """
    try:
        path = base_path + _files['departments']
        with open(path, "r") as file:
            pass
    except FileNotFoundError:
        sys.exit(f"File {_files['departments']} not Found...\nProgram will close")

    return Hospital

def menu(selop: str):
    clear()
    
    match(selop):
        case "1":
            pass
        case "2":
            pass
        case "3":
            prices_to_table(SupplyPriceList)
        case _:
            print("Wrong option")

def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

if __name__ == "__main__":
    main()
