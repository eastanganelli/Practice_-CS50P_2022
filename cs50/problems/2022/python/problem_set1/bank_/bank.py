def main():
    salutate: str = input("Greeting: ")

    salutate = salutate.lower()

    if salutate.startswith("hello"):
        print("$0")
    elif salutate.startswith("h"):
        print("$20")
    elif salutate.strip() != "":
        print("$100")

if __name__ == "__main__":
    main()