"""
Reading and writing CSV files
"""

from library.hospital import Building, Floor

class file_hospital:
    
    def read_hospital() -> dict[str, Building]:
    
        with open(".\data\hospital.csv", "r") as file:
            _MyBuilding: dict[str, Floor, dict[str, int]] = dict()
            _Flag: bool = False
            
            for line in file:
                building, floor, department, assignedmedics = line.rstrip().split(",")
                
                if _Flag:
                    _idFloor: str = str(building) + str(floor)
                    
                    if _idFloor not in _MyBuilding:
                        _MyBuilding.update({ _idFloor, Floor(department, assignedmedics), dict() })
                        
                else: _Flag = True

        return _MyBuilding

    def file_graph():
        pass

if __name__ == "__main__":
    exit(-1)