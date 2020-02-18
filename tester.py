from pattern import Object

if __name__ == "__main__":
    add_tester()


class Tester(Object):
    def __init__(self, name: str, surname: str, age: int, skill: str):
        Object.__init__(self, name, surname, age, skill)
        self.__skill: str = skill


def add_tester():
    try:
        name = str(input("Enter tester name: "))
        surname = str(input("Enter tester surname: "))
        age = int(input("Enter tester age: "))
        skill = str(input("Enter tester skill: "))
        new_tester = Tester(name, surname, age, skill)
        return new_tester
    except:
        print("Wrong data!!!")
