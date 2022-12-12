""" Libraries Import """
from library.stack import Stack
from library.file  import read_hospital, file_graph
from library.hospital import Hospital, Floor

import networkx as nx
import matplotlib.pyplot as plt

def main() -> None:
    """ Main """
    """ _AuxHospital: dict[str, Floor, dict[str, int]] = read_hospital()
    _MyFloor: Floor = _AuxHospital["A2"]
    print(_MyFloor._Department == "General Surgery") """
    
    file_graph()
    

def function_custom() -> any:
    """ Custom Function """
    return 1

if __name__ == "__main__":
    main()
