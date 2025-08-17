import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        time1,time2=s.split("to")
    
    except ValueError:
        raise ValueError("Value Error")
    
    matches1=re.search(r"^(\d|1[0-2])(:[0-5]\d)? (AM|PM)$",time1.strip())
    if not matches1:
        raise ValueError("Value Error")
    
    hour1=int(matches1.group(1))
   
    if "AM" in time1 and hour1==12:
        hour1=0
    elif "PM" in time1:
        hour1+=12
    
    minutes1=matches1.group(2)   
    
    if minutes1 == None:
        minutes1=":00"
    
    matches2=re.search(r"^(\d|1[0-2])(:[0-5]\d)? (AM|PM)$",time2.strip())
    if not matches2:
        raise ValueError("Value Error")
    
    hour2=int(matches2.group(1))
    
    if "AM" in time2 and hour2==12:
        hour2=0
    elif "PM" in time2:
        hour2+=12
     
    minutes2=matches2.group(2) 
          
    if minutes2 == None:
        minutes2=":00"
     
    return f"{hour1:02}{minutes1} to {hour2:02}{minutes2}"
    
            
if __name__ == "__main__":
    main()