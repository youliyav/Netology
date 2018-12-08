from abc import ABC, abstractmethod


class Animal(ABC):
    name = None
    weight = 0

    def __init__(self, name, weight = 0):
        self.name = name
        self.weight = weight

    @abstractmethod
    def collect_stuff(self):
        pass


class Bird(Animal):
    def collect_stuff(self):
        print("{}'s eggs was collected".format(self.name))
        super().collect_stuff()

class Ungulate(Animal):
    def collect_stuff(self):
        super().collect_stuff()


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

    def collect_stuff(self):
        print("{} was milked".format(self.name))
        super().collect_stuff()



class Sheep(Ungulate):
    def voice(self):
        return "beeee..."

    def collect_stuff(self):
        print("{} was trimmed".format(self.name))
        super().collect_stuff()


class Goat(Ungulate):
    def voice(self):
        return "meeee..."

    def collect_stuff(self):
        print("{} was milked".format(self.name))
        super().collect_stuff()



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


for animal_farm in farm_list:
    animal_farm.collect_stuff()
    total_weight += animal_farm.weight

farm_list.sort(key=lambda x: x.weight)

print('Общий вес животных: {}, самое тяжелое животное {}'.format(total_weight, farm_list[-1].name))