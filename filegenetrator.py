Dict1={}
Dict=set()
count=0
line=0
filename=input("Enter the file name or path:")
try:
    with open(filename,'r') as file:
        for i in file:
            line+=1
    file=open(filename,'r')
    data=file.read().split()
    for word in data:
        Dict.add(word)
        if word in Dict:
            Dict1[word]=Dict1.get(word,0)+1
        for i in word:
            count+=1
except FileNotFoundError as e:
    print(f"ERROR:{e}")
else:
    print(f"The number of lines in {file.name}:{line}")
    print(f"The number of words in {file.name}:{count}")
    print(f"Dictinory:{Dict1}")    
