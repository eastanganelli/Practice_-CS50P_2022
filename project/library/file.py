"""
Reading and writing CSV files
"""

from library.hospital import Building, Floor

def read_hospital() -> dict[str, Building]:
    
    with open(".\data\hospital.csv", "r") as file:
        _MyBuildings: dict[str, Building] = { }
        _Flag: bool = False
        
        for line in file:
            building, floor, department, assignedmedics = line.rstrip().split(",")
            
            if _Flag:
                
                if building in _MyBuildings.keys():
                    _FloorAux = Floor(department, int(assignedmedics))
                    
                    if _MyBuildings[building].CountFloors() > int(floor):
                        _MyBuildings[building]._Floors.insert(int(floor), _FloorAux)
                    else:
                        _MyBuildings[building]._Floors.append(_FloorAux)
                    
                else:
                    _FloorAux: Floor = Floor(department, int(assignedmedics))
                    _ListAux: list[Floor] = [ ]
                    
                    _ListAux.append(_FloorAux)
                        
                    _BuildingAux: Building = Building(_ListAux)
                        
                    _MyBuildings.update( { building: _BuildingAux } )
                    
            else: _Flag = True

    return _MyBuildings