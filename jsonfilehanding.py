import json
with open("sample.json",'w',encoding="utf-8") as file:
    data={
        "Name":"Hari",
        "Branch":"Auto",
        "Roll_no":1
    }
    write=json.dump(data,file,indent=4)
    print(file.name,"writed sucessfully")
    file.close()
with open("sample.json",'r',encoding='utf-8') as file:
    data=json.load(file)
    print(data)
    file.close()