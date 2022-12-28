class ProductException(Exception):
    
    def __init__(self, f: any, *args: object) -> None:
        super().__init__(*args)
        self.f = f

    def __str__(self) -> str:
        return f'The amount of product is invalid'
