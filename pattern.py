if __name__ == "__main__":
    pass


class Object:
    def __init__(self, name: str, surname: str, age: int, skill: str):
        self.__name: str = name
        self.__surname: str = surname
        self.__age: int = age
        self.__skill = skill

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname
        return self.__surname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age
        return self.__age

    @property
    def skill(self):
        return self.__skill

    @skill.setter
    def skill(self, age):
        self.__skill = skill
        return self.__skill

    def info(self):
        return print("name:", self.__name, "\nsurname:", self.__surname,
                     "\nage:", self.__age, "\nskill:", self.__skill)
