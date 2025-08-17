from datetime import date
from datetime import datetime
import inflect
import sys

class Time:
    def __init__(self,birthday,today):
        self.birthday=birthday
        self.today=today
    
    @classmethod
    def get(cls,birthday_=None):
        try:
            if birthday_ is None:
                birthday=date.fromisoformat(input("Date of birth:"))
            
            else: 
                birthday=date.fromisoformat(birthday_)
            
            today=date.today()
            
        except ValueError:
            sys.exit("Invalid Format")
            
        return cls(birthday,today)
    
                
    def minutes(self):       
        bd_dt= datetime.combine(self.birthday,datetime.min.time())
        td_dt= datetime.combine(self.today,datetime.min.time())
        
        delta=td_dt-bd_dt
        return round(delta.total_seconds()/60)
         
def main():
    t=Time.get()
    min=t.minutes()
    p = inflect.engine()
    print(f"{p.number_to_words(min, andword="")} minutes")
    
    
    
if __name__ == "__main__":
    main()
   
        
