import os
from input_table import import_table
from show import show
command = input("inter a command:")
if command == "add":
    import_table()
elif command == "delete" or command=="done":
    print("delete")
elif command == "show":
    data=input("inter datatime (Example jun,29,2023):")
    show(data)
else:
    print("not fond command")