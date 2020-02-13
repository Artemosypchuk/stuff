if __name__ == "__main__":
    pass


class Object:
    def __init__(self, name: str, surname: str, age: int,):
        self.__name: str = name
        self.__surname: str = surname
        self.__age: int = age

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

    def info(self):
        print(self.__name, self.__surname, self.__age)
