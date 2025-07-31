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

date=input()

if any (c.isalpha for c in date):
    mondate,year=date.split(",")
    mon,day=mondate.split()
    year=int(year)
    mon=str(mon)
    day=int(day)
    
    for i, value in enumerate(months):
        if mon == value:
            m = i+1
        
    if day<31:
        print(f"{year}-{m:02}-{day:02}")

else:
    x,y,z=date.split("/")
    x=int(x)
    y=int(y)
    z=int(z)
    if y<31:
        print(f"{z}-{x:02}-{y:02}")
    
    
    
    
    
    

    