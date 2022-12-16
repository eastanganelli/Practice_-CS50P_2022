import json

""" Libraries Import """
from library.stack import Stack
from library.file  import read_hospital
from library.hospital import Hospital, Floor

def main() -> None:
    """ Main """
    """ _AuxHospital: dict[str, Floor, dict[str, int]] = read_hospital()
    _MyFloor: Floor = _AuxHospital["A2"]
    print(_MyFloor._Department == "General Surgery") """
    
    with open(".\\data\\hospital.json", "r") as file:
        data = json.load(file)
    

def function_custom() -> any:
    """ Custom Function """
    return 1

if __name__ == "__main__":
    main()
