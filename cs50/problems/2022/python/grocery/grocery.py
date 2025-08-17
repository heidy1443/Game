grocery={}

while True:
    try:
        item=input("item:").upper()
        if item in grocery:
            grocery[item]+=1
        
        else:
            grocery[item]=1
        
        
    except EOFError:
        for item in sorted(grocery):
            print(grocery[item],item)
        
        break
            
    
    except KeyError:
        pass
    
    
        
    


        

