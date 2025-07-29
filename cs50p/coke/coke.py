due=50
while due>0: 
    insert=int(input("insert coin:"))
    if insert==5 or insert==10 or insert==25:
        due=due-insert
        if due>0:
            print("Amount due:",due)
    
    else:
        print("Amount due:",due)
        
print("change owned:",abs(due))
