def countdown():
    n = int(input("How many seconds left for Boom? "))

    while n > 0:
        print(n)
        n -= 1

    print("Boom!")

countdown()

