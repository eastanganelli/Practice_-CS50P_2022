"""
Reading and writing CSV files
"""

import json

from hospital import Floor, Hospital


""" def read_hospital() -> dict[str, Floor, list[str, int]]: """
def read_hospital() -> None:
    
    

        _coordinates: tuple[float, float] = (float(data["coordinates"]["x"]), float(data["coordinates"]["y"]))
        _Hospital: Hospital = Hospital(data["name"], data["street"],data["phone"], _coordinates )

        _Building: dict[str, Floor, list[str, int]] = { }
        for _Block in data["buildings"]:
            for _Floor in _Block["floors"]:
                _idFloor: str = _Block["block"] + str(_Floor["floor"])

                if _idFloor not in _Building:
                    _Building[_idFloor] = []

                    for _connected in _Floor["connected_to"]:
                        _idConnected: str = _connected["block"] + str(_connected["floor"])
                        _Building[_idFloor].append({ _idConnected, int(_connected["cost"]) })


if __name__ == "__main__":
    read_hospital()
