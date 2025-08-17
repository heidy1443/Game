import sys 
from PIL import Image
import os

try:
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")

    image_name,student_pic=sys.argv[1],sys.argv[2]

    if not image_name.endswith((".jpg",".jpeg",".png")) or not student_pic.endswith((".jpg",".jpeg",".png")):
        sys.exit("Invalid output") 
    
    name,ext=name, ext = os.path.splitext(image_name)
    name1,ext1=name, ext = os.path.splitext(student_pic)
    
    if ext.lower()!=ext1.lower():
        sys.exit("Input and output have different extensions")
    
    student=Image.open(sys.argv[1])
    shirt=Image.open("shirt.png")
    size = shirt.size
    student=student.resize(size)
    student.paste(shirt, shirt)
    student.save(sys.argv[2])
    
    
except FileNotFoundError:
    sys.exit("Input does not exist")
    

    
    
    
    





