class Person :
    name = "Anonymous"

    #def changeName(self,name) :
        #self.__class__.name = "Aman"

    @classmethod
    def changeName(cls , name) :
        cls.name = name;
        


p1 = Person()
p1.changeName("Aman")
print(p1.name)
print(Person.name)