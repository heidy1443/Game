def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)<2 and len(s)>6:
        return False
    
    if not s[0].isalpha() and not s[1].isalpha():
        return False
    
    if not s.isalnum():
        return False   
    
    for n in s:
        if any n.isdigit():
            
    
    else:
        return True
      


main()