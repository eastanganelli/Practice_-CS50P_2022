import sys
from library.supply import Supply, read_supply_list, prices_to_table

base_path: str = ".\\data\\"

def main() -> None:
    SupplyPriceList: list[Supply] = list()

    init_supply()
    
    
def init_supply(file_name: str = "pricelist.csv") -> list[Supply]:
    try:
        path: str = base_path + file_name
        with open(path, "r") as file:
            SupplyPriceList = read_supply_list(file)
            prices_to_table(SupplyPriceList)
    except FileNotFoundError:
        sys.exit("File not Found, program can´t continue...")

if __name__ == "__main__":
    main()
