def main():
    greeting=input().lower()
    m=value(greeting)
    print(m)


def value(g):
    if g.startswith("hello") or g.startswith("Hello"):
        return 0
    
    elif g.startswith("h") or g.startswith("H"):
        return 20

    else:
        return 100


if __name__ == "__main__":
    main()






