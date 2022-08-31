import re
from decimal import Decimal

fuel_lvl: dict[str, str] = { '0.0': "E", '0.25': "25%", '0.5': "50%", '0.75': "75%", '1.0': "F" }
mask: str = "\d+(\.{1}\d+)"

def main() -> None:
    input_splitter()

def input_splitter() -> None:
    while True:
        try:
            x, y =  input("Fraction: ").split('/')

            if(re.match(mask, x) is not None and re.match(mask, y) is not None):
                raise ValueError
            
            if(int(x) < 5 and (int(y) == 2 or int(y) == 4)):
                print(fuel_lvl[str(int(x)/int(y))])
                break

        except ValueError:
            pass
        except ZeroDivisionError:
            pass

if __name__ == "__main__":
    main()


# https://stackoverflow.com/questions/19965018/python-decimal-checking-if-integer