months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date=input("date:")
        
        if any(c.isalpha() for c in date):
            mondate,year=date.split(",")
            mon,day=mondate.split()
            year=int(year)
            mon=str(mon)
            day=int(day)
    
            for i, value in enumerate(months):
                if mon == value:
                    m = i+1
                
            if day>31:
                pass
            
            else:
                print(f"{year}-{m:02}-{day:02}")
                break

        else:
            x,y,z=date.split("/")
            x=int(x)
            y=int(y)
            z=int(z)
            
            if x>12 and y>31:
                pass
            
            else:
                print(f"{z}-{x:02}-{y:02}")
                break
        
    except ValueError:
        pass
    
    
    
    
    
    

    