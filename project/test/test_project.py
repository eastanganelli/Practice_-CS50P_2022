import pytest

from library.hospital import Hospital

def test_hospital_init() -> None:
    """ Function custom Testing """
    with pytest.raises(ValueError):
        myHospital: Hospital = Hospital(None, "Backer Street 12", "+54 911 456512")

def test_a() -> None:
    pass