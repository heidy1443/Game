words=input()
vowels=["a","e","i","o","u"]
novowels=""

for word in words:
    if word not in vowels:
        novowels+=word
print (novowels)
    
