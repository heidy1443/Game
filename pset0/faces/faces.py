def convert(text):
    text=text.replace(":)","🙂")
    text=text.replace(":(","🙁")
    return text

def main():
    say=input("Say something: ")
    print(convert(say))

main()