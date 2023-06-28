import csv
def show(data):
    mon = data[:3]
    day = data[4:6]
    yers = data[7:]

    file = open("table-work.csv",'r')
    reader = csv.reader(file)
    for row in reader:
        if mon == row[0]:
            if day == row[1]:
                if yers == row[2]:
                    print("\n\ntitel:",row[3],"\n    caption:", row[4])