import pandas as pd

class Smoothie:
    __prices = pd.read_csv('prices.csv', header=None, index_col=0, squeeze=True).to_dict()
    
    ingredients = []

    def __init__(self, ingred):
        self.ingredients = ingred

    def get_name(self):
        self.ingredients.sort()
        name = ""
        for i in range(len(self.ingredients)):
            if self.ingredients[i].endswith("ies"):
                name = name + self.ingredients[i].replace("ies", "y") + " "
            else:
                name = name + self.ingredients[i] + " "
        if len(self.ingredients) > 1:
            name += "Fusion"
        else:
            name += "Smoothie"
        return name

    def get_price(self):
        price = float(self.get_cost().replace("$", "")) * 2.5
        return "$%.2f" % price

    def get_cost(self):
        cost = 0.0
        for item in self.ingredients:
            cost += float(self.__prices[item].replace("$", ""))
        return "$%.2f" % cost

ban = Smoothie(["Strawberries", "Banana", "Blueberries"])
bom = Smoothie(["Mango"])
print("\tban")
print(ban.get_name())
print(ban.get_cost())
print(ban.get_price())
print("\tbom")
print(bom.get_name())
print(bom.get_cost())
print(bom.get_price())