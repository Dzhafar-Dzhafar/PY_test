class World:
    Class = None  # Класс объекта
    Area = None  # Среда обитания
    Affiliation = None  # Принадлежность
    Garment = None  # Тип одежды

    def __init__(self, Class, Area, Affiliation, Garment) -> None:
        self.Class = Class
        self.Area = Area
        self.Affiliation = Affiliation
        self.Garment = Garment

    def get_info(self):
        print("Класс объекта:", self.Class, " Среда обитания:", self.Area, " Принадлежность:", self.Affiliation,
              " Тип одежды:", self.Garment)


class HaraNaruna(World):  # Класс наследник
    FishFrom = None
    WaterBubble = "Blue"

    def __init__(self, FishFrom, Class, Area, Affiliation, Garment) -> None:
        super(HaraNaruna, self).__init__(Class, Area, Affiliation, Garment)
        self.FishFrom = FishFrom
        print("Образ рыбы:", FishFrom, end='  ')

    def get_info(self):
        super().get_info()
        print("Пузыри воды", self.WaterBubble)  # ПОИМОРФИЗМ - дополнение метода класса родителя, через класс наследника


class KotoTank(World):  # Класс наследник
    CatForm = None

    def __init__(self, CatForm, Class, Area, Affiliation, Garment) -> None:
        super(KotoTank, self).__init__(Class, Area, Affiliation, Garment)
        self.CatForm = CatForm
        print("Образ кота:", CatForm, end='  ')


class CatBite(KotoTank):  # Класс наследник наследника
    CatBiter = None

    def __init__(self, CatBiter, CatForm, Class, Area, Affiliation, Garment) -> None:
        super(CatBite, self).__init__(CatForm, Class, Area, Affiliation, Garment)
        self.CatBiter = CatBiter
        print("Кусь кота:", CatBiter, end='  ')


class PeroPero(World):
    pass


HaraNaruna = HaraNaruna("Yes", "Light", "Water", "South", "Light")
HaraNaruna.get_info()
CatBite = CatBite("Yes", "No", "Heavy", "Ground", "West", "Heavy")
CatBite.get_info()
PeroPero = PeroPero("Intelligence", "Air", "South", "Light")
# PeroPero.get_info()