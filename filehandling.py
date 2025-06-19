import os
import json
class OptionError(Exception):
    """rasie OptionError when gives invalid option """
    pass
print("1.csv\n2.txt\n3.json")
try:
    ch=int(input("Enter your choice:"))
    if (ch==1):
        file=open("sample1.csv",'+a')
    elif(ch==2):
        file=open("sample1.txt",'+a')
    elif(ch==3):
        file=open("sample1.json",'+a')
    else:
        raise OptionError("Your are choose Invalid option")
except OptionError as e:
    print("ERROR:",e)   
except ValueError as e:
    print("ERROR:",e)
else:    
    print(file.name,"file created sucessfully")