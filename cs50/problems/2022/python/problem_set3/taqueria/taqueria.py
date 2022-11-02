menu: dict[str, int] = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    sum: float = 0

    while(True):
        try:

            input_product: str = input("Item: ").title()
            ret_value: float = get_product(input_product)
            
            if ret_value != 0.0:
                sum += ret_value
                print("Total: $", "{:.2f}".format(sum))

        except EOFError:
            print("")
            return

def get_product(key_search: str) -> float:
    try:

        ret_value: float = menu[key_search]

    except KeyError:
        return 0.0
    else:
        return ret_value

if __name__ == "__main__":
    main()