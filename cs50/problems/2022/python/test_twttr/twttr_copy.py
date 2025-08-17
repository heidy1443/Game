vowels=["a","e","i","o","u","A","E","I","O","U"]
def main():
    words=input("input:")
    new_word=shorten(words)
    print(new_word)
       
def shorten(words):
    new=""
    for char in words:
        if char not in vowels:
            new+=char
    return new
    
    
if __name__ == "__main__":
    main()