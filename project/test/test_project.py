import pytest
from project import function_custom
from library.stack import Stack
from library.file  import read_hospital
from library.hospital import Floor, Building, Hospital

def test_function() -> None:
    """ Function Testing """

def test_custom_function() -> None:
    """ Function custom Testing """
    # with pytest.raises(ValueError):
    assert function_custom() == 1
        
def test_custom_stack() -> None:
    """ Testing Stack """
    miPilita: Stack = Stack()

    for i in range(7):
        miPilita.push(i)
        
    for i in reversed(range(7)):
        assert i == miPilita.pop()._Value

def test_custom_read_hospital() -> None:
    """ Testing Read_Hospital Function """
    
    _AuxHospital: dict[str, Building] = read_hospital()
    
    _MyFloor: Floor = _AuxHospital["A"]._Floors[2]
    
    assert _MyFloor._Department == "General Surgery"