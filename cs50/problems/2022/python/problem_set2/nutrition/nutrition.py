fruits: list[dict[str, int]] = [
    { 'fruit': "apple", 'calories': 130 },
    { 'fruit': "avocado", 'calories': 50 },
    { 'fruit': "banana", 'calories': 110 },
    { 'fruit': "cantaloupe", 'calories': 50 },
    { 'fruit': "grapefruit", 'calories': 60 },
    { 'fruit': "grapes", 'calories': 90 },
    { 'fruit': "honeydew melon", 'calories': 50 },
    { 'fruit': "kiwifruit", 'calories': 90 },
    { 'fruit': "lemon", 'calories': 15 },
    { 'fruit': "lime", 'calories': 20 },
    { 'fruit': "nectarine", 'calories': 60 },
    { 'fruit': "orange", 'calories': 80 },
    { 'fruit': "peach", 'calories': 60 },
    { 'fruit': "pear", 'calories': 100 },
    { 'fruit': "pineapple", 'calories': 50 },
    { 'fruit': "plums", 'calories': 70 },
    { 'fruit': "strawberries", 'calories': 50 },
    { 'fruit': "sweet cherries", 'calories': 100 },
    { 'fruit': "tangerine", 'calories': 50 },
    { 'fruit': "watermelon", 'calories': 80 }
]

def main():
    in_: str = input("Item: ").lower()
    response_ = get_calories(in_)
    
    if response_ != 0:
        print("Calories", response_)
    
def get_calories(fruit_: str):
    for fruit in fruits:
        if fruit['fruit'] == fruit_:
            return fruit['calories']
    
    return 0

if __name__ == "__main__":
    main()