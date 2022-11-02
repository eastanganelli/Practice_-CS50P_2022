grocery: dict[str, int] = {}

def main() -> None:
    while(True):
        try:

            item: str = input()
            sum_grocery(item.lower())

        except EOFError:
            print("")
            print_grocery()
            return

def sum_grocery(key_fruit: str) -> None:
    try:
        grocery[key_fruit]
    except KeyError:
        grocery.update({ key_fruit: 1 })
    else:
        grocery[key_fruit] += 1

def print_grocery() -> None:
    for item_ in grocery:
        print(f"{grocery[item_]} {item_.upper()}")


if __name__ == "__main__":
    main()