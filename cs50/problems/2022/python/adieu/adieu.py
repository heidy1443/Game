names=[]

while True:
    try:
        name=input("Name:")
        names.append(name)   
          
    except EOFError:
        if len(names)==1:
            new_name=names[0]
        
        elif len(names)==2:
            new_name=f"{names[0]} and {names[1]}"
        
        else:
            new_name=f"{", ".join(names[:-1])}, and {names[-1]}"
            
        print(f"Adieu, adieu, to {new_name}")
        break
        
        
    