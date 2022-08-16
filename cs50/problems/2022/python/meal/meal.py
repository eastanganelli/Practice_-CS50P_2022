def main():
    time = input("Enter time: ")

    converter(time)

def converter(time):
    hour, minutes = time.split(":")
    
    if (int(hour) == 7 and 0 <= int(minutes) < 60) or (int(hour) == 8 and int(minutes) == 0):
        print("breakfast time")
    elif (int(hour) == 12 and 0 <= int(minutes) < 60) or (int(hour) == 13 and int(minutes) == 0):
        print("lunch time")
    elif (int(hour) == 18 and 0 <= int(minutes) < 60) or (int(hour) == 19 and int(minutes) == 0):
        print("dinner time")

if __name__ == "__main__":
    main()