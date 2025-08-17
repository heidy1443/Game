camel=input()
snake=""
for idx,values in enumerate(camel):
    if camel[idx].isupper():
        snake+="_"+camel[idx].lower()
    
    else:
        snake+=camel[idx]
print(snake)
        
        

        
        
    
    
    