""" Libraries Import """
from library.stack import Stack
from library.file  import read_hospital
from library.hospital import Hospital, Building, Floor

def main() -> None:
    """ Main """
    _AuxHospital: dict[str, Building] = read_hospital()
    
    _MyFloor: Floor = _AuxHospital["A"]._Floors[2]
    
    print(_MyFloor._Department == "General Surgery")

def function_custom() -> any:
    """ Custom Function """
    return 1

if __name__ == "__main__":
    main()
