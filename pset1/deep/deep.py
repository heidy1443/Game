ans=input("what is the answer to the Great Question of Life, the Universe and Everything?")

if ans=="42":
    print("True")

elif ans.lower()=="forty two" or ans.lower()=="forty-two":
    print("True")

else:
    print("False")