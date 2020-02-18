# CLASS WORK 10
from dev import Dev, add_dev
from tester import Tester, add_tester
from ba import Ba, add_ba
from hr import Hr, add_hr


from pattern import Object
import json

emploee_list = []


def write_json(emploees_dict):
    try:
        data = json.load(open("emploees.txt"))
    except:
        data = []
    data.append(emploees_dict)
    with open("emploees.txt", 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def read_json(x):
    try:
        emploee_list = list()
        with open("emploees.txt") as file:
            emploee_list = json.load(file)
        for item in emploee_list:
            if x == 1:
                print("-"*50)
                for key, value in item.items():
                    print(key, ":", value)
            elif x == 2:
                new_id = emploee_list[len(emploee_list) - 1]['id']
                return new_id
    except Exception as err:
        print('File not exist! or ', err)


def del_employee(x):
    try:
        emploee_list = list()
        with open("emploees.txt") as file:
            emploee_list = json.load(file)
        for item in emploee_list:
            for key, value in item.items():
                if value == x and key == "id":
                    if item in emploee_list:
                        emploee_list.remove(item)
        with open("emploees.txt", 'w') as file:
            json.dump(emploee_list, file, indent=2, ensure_ascii=False)
    except Exception as er:
        print("Problem", er)


def create_emploe(em):
    empl = em()
    try:
        emploee_list = []
        id_count = read_json(2)
        id_count += 1
        person = {"id": id_count, "name": empl.name,
                  "surname": empl.surname, "age": empl.age, "skill": empl.skill}
        write_json(person)
    except:
        emploee_list = []
        id_count = int(len(emploee_list))+1
        person = {"id": id_count, "name": empl.name,
                  "surname": empl.surname, "age": empl.age, "skill": empl.skill}
        write_json(person)


while True:
    try:
        print("""
                "WELLCOME TO FIRM"
            1: Show employees
            2: Kill some employee
            3: Show employee info you need
            4: Add employee
            0: Exit
        """)
        menu_check = int(input(": "))
        if menu_check == 0:
            print("GOOD BYE MTHFKR-)")
            break
        elif menu_check == 99:
            for i in range(0, 10):
                for x in range(0, 10):
                    print('*', end="<>")
                print()
                print('-'*20)
        elif menu_check == 1:
            read_json(1)
        elif menu_check == 2:
            print("Enter employees ID to kill him!=)")
            returned = del_employee(int(input(": ")))
            print(returned)
        elif menu_check == 3:
            read_json(2)
        elif menu_check == 4:
            while True:
                try:
                    print("""
                            Add emploee:
                                1:  + Add Dev
                                2:  + Add Tester
                                3:  + Add BA
                                4:  + Add HR
                                0: <===Back previos menu
                        """)
                    add_check = int(input())
                    if add_check == 0:
                        break
                    elif add_check == 1:
                        create_emploe(add_dev)
                    elif add_check == 2:
                        create_emploe(add_tester)
                    elif add_check == 3:
                        create_emploe(add_ba)
                    elif add_check == 4:
                        create_emploe(add_hr)
                except Exception as err:
                    print('Inner error:', err)
    except Exception as err:
        print("Out error:", err)
