class Hugo:
    def __init__(self):
        self.__name = "Hugo"
        self.__age = 23
    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age
    @name.setter
    def name(self, name):
        self.__name = name
    @age.setter
    def age(self, age):
        self.__age = age

h = Hugo()
h.name = "print"
print(h.name)

