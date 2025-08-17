import random

def main():
    try:
        level=int(input("level:"))
        lv=get_level(level)
    except ValueError:
            pass
    
    counts=0
    problem=0      
           
    while problem<10: 
        
            x,y=generate_integer(lv)
            target=x+y
            attempt=0
            
            while attempt<3:
                try:
                    answer=(int(input(f"{x}+{y}=")))
                    if answer==target:
                        counts+=1
                        break
                    
                    else:
                        attempt+=1
                        print("EEE")
                    
                except ValueError:
                    print("EEE")
                    attempt+=1
                    
            if attempt==3:
                print(f"{x}+{y}={target}")
            
            problem+=1
                
                        
    print("score:",counts)


def get_level(level):
    while level not in [1,2,3]:
        level=int(input("level:"))
    return level
        

def generate_integer(level):
    
    if level ==1:
        x=random.randint(0,9)
        y=random.randint(0,9)
        return x,y
    
    if level==2:
        x=random.randint(10,99)
        y=random.randint(10,99)
        return x,y
    
    if level==3:
        x=random.randint(100,999)
        y=random.randint(100,999)
        return x,y
        
    
if __name__ == "__main__":
    main()