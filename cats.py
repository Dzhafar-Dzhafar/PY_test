class Cats:
    name = None
    age = None
    isHappy = None

    def set_data(self, name, age, isHappy): #За счет "self" обращаться сможем к параметрам внутри класса
        self.name = name
        self.age = age
        self.isHappy = isHappy
    def get_data(self): #set_data и get_data - это функции (вне класса) или методы (внутри класса).
        print("Имя:", self.name, '|', "age:", self.age, '|', "Happy:", self.isHappy)

cat1 = Cats()
cat1.set_data('Bobo', 3, True)
# ИЛИ
cat2 = Cats()
cat2.name = "Kukuy"
cat2.age = 2
cat2.isHappy = False

cat1.get_data()
cat2.get_data()