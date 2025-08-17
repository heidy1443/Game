while True:    
    try:
        fra=input("Fraction:")
        x,y=fra.split("/")
        x=int(x)
        y=int(y)
        result=100*(x/y)
        
        if x> y or x< 0:
            pass 
        
        elif result<1 and result>=0:
            print("E") 
            break 
        
        elif result>99 and result<=100:
            print("F")
            break
        
        elif result>0 or result<100:
            print(round(result),"%")
            break
    
    except ValueError:
        pass
    
    except ZeroDivisionError:
        pass
    
    
        
    

