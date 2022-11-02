import re
from decimal import Decimal
import math

mask: str = "\d+(\.{1}\d+)"

def main() -> None:
    input_splitter()

def input_splitter() -> None:
    while True:
        try:
            x, y =  input("Fraction: ").split('/')

            if(re.match(mask, x) is not None and re.match(mask, y) is not None):
                raise ValueError

            value_: int = int(int(x)/int(y)*100)

            if ( int(x)/int(y)*100 - int(int(x)/int(y)*100) ) > 0.5:
                value_ = math.ceil(int(x)/int(y)*100)

            if value_ > 100:
                raise ValueError

        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            if value_ > 95:
                print("F")
            elif value_ < 5:
                print("E")
            else:
                print(f"{value_}%")

            return

if __name__ == "__main__":
    main()


# https://stackoverflow.com/questions/19965018/python-decimal-checking-if-integer