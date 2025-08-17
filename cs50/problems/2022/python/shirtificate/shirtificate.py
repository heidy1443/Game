from fpdf import FPDF
import sys

class Shirt(FPDF):
    def __init__(self, name):
        super().__init__()
        self.name=name
    
    @classmethod
    def get(cls):
        name=input("What's your name?")
        
        if " " in name:
            first,last=name.split(" ")
            if not first.isalpha() or not last.isalpha():
                sys.exit("Not a name.")
        elif not name.isalpha():
            sys.exit("Not a name.")
            
        return cls(name)
        
    def header(self):
        self.set_font("Times", style="B", size=50)
        self.cell(0,40, 'CS50 Shirtificate', align="C")
        self.ln(20)
       
    
    def name_shirt(self):       
        self.set_font("helvetica", style="B", size=25)
        self.set_text_color(255,255,255)
        self.set_y(120)
        text=f"{self.name} took CS50"
        text_width=self.get_string_width(text)+8
        self.set_x((self.w-text_width)/2)
        self.set_draw_color(255,100,150)
        self.cell(text_width,20,text,border=1,align="C")
        
                
def main():
    shirt=Shirt.get()
    shirt.add_page()
    shirt.image("shirtificate.png",x=10,y=60,w=shirt.epw, keep_aspect_ratio=True)
    shirt.name_shirt()
    shirt.output("shirt_with_name.pdf")
    
if __name__=="__main__":  
    main()        
