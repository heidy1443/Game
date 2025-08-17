import random


while True:
    try:
        level=int(input("level:")) 
        if level>0:
            pass
        
    except ValueError:
        pass
    
    number=random.randint(1,level)
    while True:    
        try:
            
        
            guess=int(input("guess:"))
        
            if guess>0 and guess== number:
                print("Just right!")
                break
        
            elif guess>0 and guess>number:
                print("Too large!")
        
            elif guess>0 and guess<number:
                print("Too small!")
        
        except ValueError:
            pass
    break
    
        
        