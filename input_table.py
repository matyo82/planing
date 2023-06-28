import csv
def import_table():
    # Getting information from the user
    date = input("Date of work(Example jun,29,2023):")
    data2 = "kwn"
    titel = input("The title of doing the work:")
    caption = input("Description:")
    file_name = "table-work.csv"
    try:
        open(file_name)
    except:
        print("not fine file!!")

    file = open(file_name,"+a")
    data = [date,titel,caption]
    writer = csv.writer(file)
    writer.writerow(data)
    file.close()