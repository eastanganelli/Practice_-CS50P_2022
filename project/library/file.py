"""
Reading and writing CSV files
"""

from library.hospital import Floor


def read_hospital() -> dict[str, Floor, dict[str, int]]:
    
    _MyBuilding: dict[str, Floor, list[str, int]]
    _Flag: bool = False
    
    with open(".\\data\\hospital.csv", "r") as file:
                    
        for line in file:
            building, floor, department, assignedmedics = line.rstrip().split(",")
            
            if _Flag:
                _idFloor: str = str(building) + str(floor)
                
                if _idFloor not in _MyBuilding:
                    _MyBuilding.update({ _idFloor, Floor(department, assignedmedics), [] })
                    
            else: _Flag = True

    return _MyBuilding

def file_graph():
    
    _MyGraph: dict[str, list[str, int]]
    
    with open(".\\data\\building_graph.csv") as file:
        
        for line in file:
            building,floor,building_connected,floor_connected,distance = line.rstrip().split(",")
            
            _fromFloor: str = building + floor
            _toFloor: str = building + floor
            
            if _fromFloor not in _MyGraph:
                _MyGraph[_fromFloor] = []
            if _toFloor not in _MyGraph:
                _MyGraph[_toFloor] = []
            
            # Undirected Graph
            _MyGraph[_fromFloor].append(( _toFloor, int(distance) ))
            _MyGraph[_toFloor].append(( _fromFloor, int(distance) ))
            

if __name__ == "__main__":
    exit(-1)