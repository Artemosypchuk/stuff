from pattern import Object

if __name__ == "__main__":
    add_hr()


class Hr(Object):
    def __init__(self, name: str, surname: str, age: int, skill: str):
        Object.__init__(self, name, surname, age, skill)
        self.__skill: str = skill


def add_hr():
    try:
        name = str(input("Enter HR name: "))
        surname = str(input("Enter HR surname: "))
        age = int(input("Enter HRage: "))
        skill = str(input("Enter HR skill: "))
        new_hr = Hr(name, surname, age, skill)
        return new_hr
    except:
        print("Wrong data!!!")
