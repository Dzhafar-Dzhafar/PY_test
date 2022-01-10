class Cats:
    name = None
    age = None
    isHappy = None

    def __init__(self, name=None, age=None, isHappy=None):
        self.set_data(name, age, isHappy)
        '''
        self.name = name
        self.age = age
        self.isHappy = isHappy
        '''
        self.get_data()

    def set_data(self, name=None, age=None, isHappy = None): #За счет "self" обращаться сможем к параметрам внутри класса
        self.name = name
        self.age = age
        self.isHappy = isHappy
    def get_data(self): #set_data и get_data - это функции (вне класса) или методы (внутри класса).
        print("Имя:", self.name, '|', "age:", self.age, '|', "Happy:", self.isHappy)

cat1 = Cats('Bobo', 3, True)
#cat1.set_data('Bobo', 3, True)

cat1.set_data('jone', 2)

cat2 = Cats("Kukuy", 2, False)
'''
cat2.name = "Kukuy"
cat2.age = 2
cat2.isHappy = False
'''