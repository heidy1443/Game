def main():
    while True:
        fra=input("Fraction:")
        p=convert(fra)
        result=gauge(p)
        print(result)
        break
        
    
def convert(fraction):
    x,y=fraction.split("/")
    x=int(x)
    y=int(y)
    percent=100*(x/y)
    
    if x<0 or y<0:
        raise ValueError("Negative numbers are not available.")
    
    elif y==0:
        raise ZeroDivisionError("Can't divide by zero.")
    
    elif x>y:
        raise ValueError("x can't be greater than y.")
    
    else:
        return round(percent)
    
    
def gauge(percentage):
    percentage=int(percentage)
    
    if percentage<1 and percentage>=0:
        return "E"
    
    elif percentage>99 and percentage<=100:
        return "F"
    
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()


    
        
    

