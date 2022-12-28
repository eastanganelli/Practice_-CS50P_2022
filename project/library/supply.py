from tabulate import tabulate
from library.exceptions import ProductException

class Supply:
    
    
    def __init__(self, Name: str, Price: int):
        if not Name:
            raise ValueError
        
        if not Price:
            raise ValueError

        self.__Name = Name
        self.__Price = Price

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str) -> None:
        self.__Name = Name

    @property
    def Price(self) -> int:
        return self.__Price

    @Price.setter
    def Price(self, Price: int) -> None:
        self.__Price = Price

    def __str__(self) -> str:
        return f"{self.__Name} : {self.__Price}"

    def buy_product(self, amount: int) -> int:
        if not amount:
            raise ValueError

        return self.__Price * amount

    def sell_product(self, amount: int) -> int:
        if not amount:
            raise ValueError

        return self.__Price * amount

    def buy_product(self, actual_amount: int) -> int:
        if actual_amount < 1:
            raise ProductException(actual_amount)
        


def read_supply_list(SupplyFile: any) -> list[str, int]:
    priceList: list[Supply] = list()

    dummy: str = None

    for line in SupplyFile:
        if dummy is None:
            dummy = line
        else:
            values = line.rstrip().split(";")

            if int(values[1]) > 0:
                priceList.append( Supply(str(values[0]), int(values[1])) )
            else:
                raise ValueError

    return priceList

def prices_to_table(list_: list[Supply]) -> None:
    aux_list: list[list[str, int]] = list()

    for myPrice in list_:
        aux_list.append( [ myPrice.Name, myPrice.Price ] )

    print(tabulate(aux_list, headers=["Product", "Price"], tablefmt="grid"))
