data="Hello World!,Welcome to Python Programming."
file=open("sample.txt",'w')
file.write(data)
file.close()
file=open("sample.txt",'r')
data=file.read()
print(data)