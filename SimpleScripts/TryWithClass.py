class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        print("Create object of class Person.")
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if 0 < age < 120:
            self.__age = age
        else:
            print("Invalid age.")
        
    @property 
    def name(self):
        return self.__name    
        
    def say_info(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        
    def __del__(self):
        print("Object was deleted")
        
person = Person("Alex", 130)
person.name = "vvv"
print(person.name)
# per.say_message("Hi, all")
# per.say_info()
# print(per._Person__name)
# per.__name = -100
# print(per.__name)
