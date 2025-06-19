import csv
data=[
    {"Name":"Hari","Branch":"Auto","Rollno":10},
    {"Name":"Surya","Branch":"Cevil","Rollno":42}
]
fields=["Name","Branch","Rollno"]
with open("sample.csv",mode='w',newline='') as file:
    print("sample.csv file created suceessfully.")
    writer=csv.DictWriter(file,fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)
with open('your_file.csv', 'r', newline='') as file:
    csv_reader = csv.reader(file)    
    header = next(csv_reader, None)
    for row in csv_reader:
        print(row)
