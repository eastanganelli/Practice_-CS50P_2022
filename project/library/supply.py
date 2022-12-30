from tabulate           import tabulate
from library.exceptions import SupplyInvalidException, SupplyInStockException

class Supply:
    MAX_: int = 25
    MIN_: int = 5
    
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

    @staticmethod
    def buy_product(price_list: list[any], MySupply: tuple[str, int]) -> tuple[int, int]:
        if 0 < MySupply[1]:
            raise SupplyInvalidException(MySupply[1])
        elif MySupply[1] >= Supply.MIN_:
            raise SupplyInStockException(MySupply[0])

        price: int = [product for product in price_list if product.Name == MySupply[0]]
        toBuy: int = Supply.MAX_ - MySupply[1]

        return toBuy, toBuy * price

    @staticmethod
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

    @staticmethod
    def prices_to_table(prices: list[Supply]) -> None:
        aux_list: list[list[str, int]] = list()

        for myPrice in prices:
            aux_list.append( [ myPrice.Name, myPrice.Price ] )

        print(tabulate(aux_list, headers=["Product", "Price"], tablefmt="grid"))
