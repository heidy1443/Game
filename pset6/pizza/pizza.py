from tabulate import tabulate
import sys
import csv

try:
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")

    file_name=sys.argv[1]

    if not file_name.endswith(".csv"):
        sys.exit("Not a CSV file")
    
    with open(file_name, newline="")as file:
        reader=csv.reader(file)
        table=list(reader)
        
    print(tabulate(table, headers="firstrow", tablefmt="grid"))
                
except FileNotFoundError:
    sys.exit("File does not exist")
    



