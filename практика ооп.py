class Animals:
    def __init__(self, dog, cat):
        self.dog = dog
        self.cat1 = cat
        
    def souds_of_animals(self, gaf, myau):
        self.gaf = gaf
        self.myau = myau
        
    def make_sound(self):
        print(self.dog, 'Make sound "{self.gaf}" ', self.cat ,'and cat make sound "{self.myau}" ')













# class Person:
#     def __init__(self, name="", age=0, city=""):
#         self.name = name
#         self.age = age
#         self.city = city

#     def set_data(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city

#     def introduce(self):
#         print(f"Привет, меня зовут {self.name}, мне {self.age} лет, я из города {self.city}.")

# # Создаём объект
# person1 = Person()
# person1.set_data("Алексей", 25, "Бишкек")
# person1.introduce()
