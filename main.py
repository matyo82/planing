import csv

# Getting information from the user
date = input("Date of work(Example jun,29,2023):")
titel = input("The title of doing the work:")
caption = input("Description:")

file_name = "table-work.csv"
try:
    open(file_name)
except:
    print("not fine file!!")

file = open(file_name,"+a",newline="")
data = [date,titel,caption]
writer = csv.writer(file)
writer.writerow(data)
file.close()