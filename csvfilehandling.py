import csv
data=[
    {"Name":"Hari","Branch":"Auto","Rollno":10},
    {"Name":"Surya","Branch":"Cevil","Rollno":42}
]
fields=["Name","Branch","Rollno"]
with open("sample.csv",mode='w',newline='') as file:
    writer=csv.DictWriter(file,fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)
