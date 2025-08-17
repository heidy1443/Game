import csv
import sys

after={}

try:
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    
    file_name=sys.argv[1]
    
    if not file_name.endswith(".csv"):
        sys.exit("Not a CSV file")
    
    with open(file_name)as file:
        reader=csv.DictReader(file)
        
        with open("after.csv","w",newline='')as out_file:
            writer=csv.DictWriter(out_file,fieldnames=["first","last","house"])
            writer.writeheader()
            for row in reader:
                first_name,last_name=row["name"].split(",")
                writer.writerow({"first":first_name.strip(),"last":last_name.strip(),"house":row["house"].strip()})
                
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

