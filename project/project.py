import signal
import readchar
import sys
import json

from library.supply     import Supply
from library.hospital   import Hospital
from library.exceptions import SupplyInStockException, SupplyInvalidException

base_path: str = ".\\data\\"
_files: dict[str, str] = {
    "pricelist": "pricelist.csv",
    "hospital": "hospital.json",
    "departments": "departments.csv"
}

def handler(signum, frame):
    msg: str = "Ctrl-c was pressed. Do you really want to exit? y/n"
    print(msg, end="", flush=True)
    response = readchar.readchar()
    if response == "y":
        exit()
    else:
        print("", end="\r", flush=True)
        print(" " * len(msg), end="", flush=True) # clear the printed line
        print("    ", end="\r", flush=True)

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
        pass
    
def init_supply() -> list[Supply]:
    try:
        path: str = base_path + _files["pricelist"]
        with open(path, "r") as file:
            SupplyPriceList = Supply.read_supply_list(file)
            Supply.prices_to_table(SupplyPriceList)
    except FileNotFoundError:
        sys.exit(f'File {_files["pricelist"]} not Found, program can´t continue...')
    else:
        return SupplyPriceList

def init_hospital() -> Hospital:
    MyHospital: Hospital = None
    
    path: str = None
    try:
        path = base_path + _files['departments']
        with open(path, "r") as file:
            pass
    except FileNotFoundError:
        sys.exit(f"File {_files['departments']} not Found...\nProgram will close")
    
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

    return Hospital    

if __name__ == "__main__":
    main()
