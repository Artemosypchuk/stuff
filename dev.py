from pattern import *

if __name__ == "__main__":
    add_dev()


class Dev(Object):
    def __init__(self, name, surname, age, skill):
        Object.__init__(self,name,surname,age)
        self.__skill = skill


def add_dev():
    try:
        name = str(input("Enter dev name: "))
        surname = str(input("Enter dev surname: "))
        age = int(input("Enter dev age: "))
        skill = str(input("Enter dev skill: "))
        new_dev = Dev(name,surname,age,skill)
        
    except:
        print("Wrong data!!!")
    finally:
        print(new_dev.info(),"Created!")
        return new_dev
    
