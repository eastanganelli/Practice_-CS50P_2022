from typing import Tuple
import re

month_list: list[str] = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

regex_MMddyyyy: str = "(January?|February?|March?|April?|May|June?|July?|August?|September?|October?|November?|December?)\s+([1-9]|[12][0-9]|3[01]),\s+\d{4}"
regex_mmddyyyy: str = "(([1-9]|1[0-2]))\/(([1-9]|[12][0-9]|3[01]))\/(\d{4})"

def main() -> None:
    year, month, day = read_input()
    date_formater(year, month, day)

def read_input() -> Tuple[str, str, str]:
    while True:
        try:
            input_str: str = input("Date: ")

            if (re.match(regex_MMddyyyy, input_str) is not None):
                ## December 12, 2022
                month_, day_, year_ = input_str.replace(",", "").split(" ")
                month_ = str(month_list.index(month_.title()) + 1)
            elif (re.match(regex_mmddyyyy, input_str) is not None):
                ## MM/DD/YYYY
                month_, day_, year_ = input_str.split("/")
            else:
                raise ValueError
        except ValueError:
            pass
        else:
            return year_, month_, day_

def date_formater(year_: str, month_: str, day_: str) -> None:
    month_ = ("0" + month_) if (int(month_) < 10 ) else None
    day_   = ("0" + day_)   if (int(day_)   < 10 ) else None
    
    ## Output -> YYYY-MM-DD
    print(f"{year_}-{month_}-{day_}")

if __name__ == "__main__":
    main()