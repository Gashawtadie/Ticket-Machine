
from supply import supplier
from timer import tim
import dictioner

tray = 0
choice = "."
while choice != "e" and tray < 3:
    enter_id = input("Enter your id please: ")
    if enter_id in dictioner.Id:
        for key, value in dictioner.departments.items():
            print(f"\t\t choose, {key} - {value} departments")
        choice = input("which of the places you wish to visit: ")
        if choice in dictioner.lists_dict:
            if len(dictioner.lists_dict[choice]) == 0:
                supplier(choice)
                print(
                    f"your number is: {choice} - {dictioner.lists_dict[choice][0]} ")
                del dictioner.lists_dict[choice][0]
            else:
                print(
                    f"your number is: {choice} - {dictioner.lists_dict[choice][0]} please wait and some one will assist you shortly.")
                del dictioner.lists_dict[choice][0]
            print("♥" * 20)

    else:
        tray += 1
        print(f"sorry you are not in the system, please try again, you have {3 - tray} chances!!")
        if tray == 3:
            print(f"sorry will see you soon")
            tim()

