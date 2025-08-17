import validators

if validators.email(input("E-mail:"))== True:
    print("Valid")

else:
    print("Invalid")
