import pytest
from project import function_custom

def test_function() -> None:
    """ Function Testing """

def test_custom_function() -> None:
    """ Function custom Testing """
    with pytest.raises(ValueError):
        assert function_custom() == 1
