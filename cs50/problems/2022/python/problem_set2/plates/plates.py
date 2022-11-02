import re

regex_plates: str = [
    "^[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][1-9][0-9]$",
    "^[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][1-9]$",
    "^[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]$",
    "^[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]$",
    "^[a-zA-Z][a-zA-Z][a-zA-Z][1-9][0-9][0-9]$",
    "^[a-zA-Z][a-zA-Z][a-zA-Z][1-9][0-9]$",
    "^[a-zA-Z][a-zA-Z][a-zA-Z][1-9]$",
    "^[a-zA-Z][a-zA-Z][a-zA-Z]$",
    "^[a-zA-Z][a-zA-Z][1-9][0-9][0-9][0-9]$",
    "^[a-zA-Z][a-zA-Z][1-9][0-9][0-9]$",
    "^[a-zA-Z][a-zA-Z][1-9][0-9]$",
    "^[a-zA-Z][a-zA-Z][1-9]$",
    "^[a-zA-Z][a-zA-Z]$"
]

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str):
    if(1 < len(s) < 7):
        for regex in regex_plates:
            res_regex = bool(re.match(regex, s))
            if res_regex:
                return True

    return False

if __name__ == "__main__":
    main()