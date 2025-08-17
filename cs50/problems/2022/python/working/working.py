import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        time1,time2=s.split("to")
    
    except ValueError:
        raise ValueError("Value Error")
    
    hour1, minutes1=match(time1)
    hour2, minutes2=match(time2)
    
    return f"{hour1:02}{minutes1} to {hour2:02}{minutes2}"
    
    
def match(n):
    matches=re.search(r"^(\d|1[0-2])(:[0-5]\d)? (AM|PM)$",n.strip())
    if not matches:
        raise ValueError("Value Error")
    
    hour=int(matches.group(1))
   
    if "AM" in n and hour==12:
        hour=0
    elif "PM" in n:
        hour+=12
    
    minutes=matches.group(2)   
    
    if minutes == None:
        minutes=":00"
    
    return hour,minutes
    

if __name__ == "__main__":
    main()
    