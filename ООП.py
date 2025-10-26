class Cat:
    name = None
    age = None
    isHappy = None

    def __init__(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    # def set_data(self, name, age, isHappy):
    #     self.name = name
    #     self.age = age
    #     self.isHappy = isHappy

    # def get_data(self):
        print(
            "Кота зовут:", self.name,
            "\nВозраст кота:", self.age,
            "\nСчастлив ли наш кот?:", self.isHappy
        )


cat1 = Cat("Жопен", 4, True)
# cat1.set_data("Жопен", 4, True)
# cat1.get_data()
