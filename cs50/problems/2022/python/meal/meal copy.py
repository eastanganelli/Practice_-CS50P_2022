def main():
    time = input("Enter time: ")

    meal_response = converter(time)
    """ meal_response = converter_12hs(time) """
    if meal_response != "":
        print(meal_response)


def converter(time):
    hour, minutes = time.split(":")
    
    if (int(hour) == 7 and 0 <= int(minutes) < 60) or (int(hour) == 8 and int(minutes) == 0):
        return "breakfast time"
    elif (int(hour) == 12 and 0 <= int(minutes) < 60) or (int(hour) == 13 and int(minutes) == 0):
        return "lunch time"
    elif (int(hour) == 18 and 0 <= int(minutes) < 60) or (int(hour) == 19 and int(minutes) == 0):
        return "dinner time"
    else:
        return ""

def converter_12hs(time):
    time, y = time.split(" ")
    hour, minutes = time.split(":")
    
    if ((int(hour) == 7 and 0 <= int(minutes) < 60) or (int(hour) == 8 and int(minutes) == 0)) and y.lower() == "am":
        return "breakfast time"
    elif ((int(hour) == 12 and 0 <= int(minutes) < 60) or (int(hour) == 1 and int(minutes) == 0)) and y.lower() == "pm":
        return "lunch time"
    elif ((int(hour) == 6 and 0 <= int(minutes) < 60) or (int(hour) == 7 and int(minutes) == 0)) and y.lower() == "pm":
        return "dinner time"
    else:
        return ""

if __name__ == "__main__":
    main()