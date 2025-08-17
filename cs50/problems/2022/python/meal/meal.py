def main():
    hour=convert(input("what time is it?"))
    if hour>=7 and hour<=8:
        print("Breakfast Time")
    
    elif hour>=12 and hour<=13:
        print ("Lunch Time")
    
    elif hour>=18 and hour<=19:
        print ("Dinner Time")


def convert(time):
    hours, minutes = time.split(":")
    hours=int(hours)
    minutes=int(minutes)/60
    return hours+minutes


if __name__ == "__main__":
    main()