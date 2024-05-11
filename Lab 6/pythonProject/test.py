class Cat:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def cat_name(self):
        return self.name

    def new_cat_name(self, value):
        self.name = value

    my_cat_name = property(fget = cat_name, fset = new_cat_name)

cat = Cat("Vasya", "British")
cat.name = "Kostya"
cat.breed = "Prostoi_Kot"