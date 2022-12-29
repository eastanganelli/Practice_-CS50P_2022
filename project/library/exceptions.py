class SupplyInvalidException(Exception):
    
    def __init__(self, msg: any) -> None:
        self.msg = msg

    def __str__(self) -> str:
        return f'The amount of Supply is invalid'

class SupplyInStockException(Exception):

    def __init__(self, msg: any) -> None:
        self._msg = msg

    def __str__(self) -> str:
        return f'The Supply {self._msg} is still in Stock'

class ProductSeletionException(Exception):
    
    def __init__(self, msg: any) -> None:
        self.msg = msg

    def __str__(self) -> str:
        return f"Product {self.f} does not Exists"