class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        print("{} was fed".format(self.name))



class Bird(Animal):
    def collect_eggs(self):
        print("{}'s eggs was collected".format(self.name))

class Ungulate(Animal):
    pass


class Goose(Bird):
    def voice(self):
        return "ga-ga-ga..."


class Chicken(Bird):
    def voice(self):
        return "ko-ko-ko..."


class Duck(Bird):
    def voice(self):
        return "krya-krya-krya..."


class Cow(Ungulate):
    def voice(self):
        return "muuuu..."

    def milk(self):
        print("{} was milked".format(self.name))


class Sheep(Ungulate):
    def voice(self):
        return "beeee..."

    def trimm(self):
        print("{} was trimmed".format(self.name))


class Goat(Ungulate):
    def voice(self):
        return "meeee..."

    def milk(self):
        print("{} was milked".format(self.name))


total_weight = 0
farm_list = []

goose_0 = Goose("Gray", 4)
farm_list.append(goose_0)

goose_1 = Goose("White", 3)
farm_list.append(goose_1)

cow_0 = Cow("Man'ka", 233)
farm_list.append(cow_0)

sheep_0 = Sheep("Barashek", 62)
farm_list.append(sheep_0)

sheep_1 = Sheep("Kudryavyi", 70)
farm_list.append(sheep_1)

chicken_0 = Chicken("Ko-ko", 2)
farm_list.append(chicken_0)

chicken_1 = Chicken("Kukareku", 3)
farm_list.append(chicken_1)

goat_0 = Goat("Roga", 45)
farm_list.append(goat_0)

goat_1 = Goat("Kopita", 47)
farm_list.append(goat_1)

duck_0 = Duck("Kryakva", 5)
farm_list.append(duck_0)

goose_0.collect_eggs()
goose_1.feed()
cow_0.milk()
sheep_0.feed()
sheep_1.trimm()
chicken_0.collect_eggs()
chicken_1.collect_eggs()
goat_0.milk()
goat_1.feed()
duck_0.collect_eggs()

def total_weight(farm_list):
  total_weight = 0
  heaviest = None
  for x in farm_list:
    total_weight += x.weight
    if heaviest == None:
      heaviest = x
    elif x.weight > heaviest.weight:
      heaviest = x
  return print('Общий вес животных: {}, самое тяжелое животное {}'.format(total_weight, heaviest.name))

total_weight(farm_list)