import csv

headers = ["Name", "Age", "Course"]
rows = [
    ["Rahul", 20, "BTech"],
    ["Priya", 21, "BCA"],
    ["Amit", 19, "BTech"]
]

with open("students.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers) 
    writer.writerows(rows)   

print("CSV file 'students.csv' created successfully!\n")


print("Reading the CSV file:")
with open("students.csv", mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
