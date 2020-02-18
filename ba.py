from pattern import Object

if __name__ == "__main__":
    add_ba()


class Ba(Object):
    def __init__(self, name: str, surname: str, age: int, skill: str):
        Object.__init__(self, name, surname, age, skill)
        self.__skill: str = skill


def add_ba():
    try:
        name = str(input("Enter BA name: "))
        surname = str(input("Enter BA surname: "))
        age = int(input("Enter BA age: "))
        skill = str(input("Enter BA skill: "))
        new_ba = Ba(name, surname, age, skill)
        return new_ba
    except:
        print("Wrong data!!!")
