# CLASS WORK 10
from dev import Dev, add_dev
from pattern import Object


emploee_list = []
while True:
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
    elif menu_check == 1:
        print(emploee_list)
    elif menu_check == 2:
        pass
    elif menu_check == 3:
        pass
    elif menu_check == 4:
        while True:
            print("""
                    Add emploee:
                        1: Add Dev
                        2: Add Tester
                        3: Add BA
                        4: Add HR
                        0: Back previos
                  """)
            add_check = int(input())
            if add_check == 0:
                break
            elif add_check == 1:
                new_dev = add_dev()
                emploee_list.append(new_dev)
