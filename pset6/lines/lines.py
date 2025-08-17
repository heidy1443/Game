import sys

try:    
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    
    file_name=sys.argv[1]
    
    if not file_name.endswith(".py"):
        sys.exit("Not a Python file")
        

    with open(file_name,"r") as file:
        lines=file.readlines()
        
    count=0
    for line in lines:
        if not line.strip().startswith("#") and not line.strip()=="":
            count+=1
    
    print(count)
            
       
except FileNotFoundError:
    sys.exit("File does not exist")



