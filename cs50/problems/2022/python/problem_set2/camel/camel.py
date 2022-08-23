snakecase: dict[str, str] = {
    'name': "name",
    'firstname': "first_name",
    'preferredfirstname': "preferred_first_name"
}

def main():
    dictionary: str = input("camelCase: ")
    dictionary = dictionary.lower()
    get_dictionary(dictionary)

def get_dictionary(dictionary):
    print("snake_case", snakecase[dictionary], sep=": ")

if __name__ == "__main__":
    main()