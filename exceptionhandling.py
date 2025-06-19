class ageerror(Exception):
    pass
try:
    age=int(input("Enter your age:"))
    if (age<18):
        raise ageerror()
    else:
        print("You are welcome")
except ageerror as e:
    print("ERROR:Your age must be more then 18")
except Exception as e:
    print("ERROR:",e)