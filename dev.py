from pattern import Object

if __name__ == "__main__":
    add_dev()


class Dev(Object):
    def __init__(self, name:str, surname:str, age:int, skill:str):
        Object.__init__(self, name, surname, age, skill)
        self.__skill:str = skill


def add_dev():
    try:
        name = str(input("Enter dev name: "))
        surname = str(input("Enter dev surname: "))
        age = int(input("Enter dev age: "))
        skill = str(input("Enter dev skill: "))
        new_dev = Dev(name, surname, age, skill)
        return new_dev
    except:
        print("Wrong data!!!")
