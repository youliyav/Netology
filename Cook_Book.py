def read_file(path):
    cook_book = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            name_dish = line.strip()
            cook_book[name_dish] = []
            count = f.readline()
            for element in range(int(count)):
                ingrid_list = f.readline().strip().split("|")
                ingrid_dict = {"ingridient_name": ingrid_list[0], "quantity": int(ingrid_list[1]), "measure": ingrid_list[2]}
                cook_book[name_dish].append(ingrid_dict)
            f.readline()
        return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_file("cook_book.txt")
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list = dict(ingridient)
            new_shop_list["quantity"] *= person_count
            if new_shop_list["ingridient_name"] not in shop_list:
                shop_list[new_shop_list["ingridient_name"]] = {"measure": new_shop_list["measure"], "quantity": new_shop_list["quantity"]}
            else:
                shop_list[new_shop_list["ingridient_name"]["quantity"]] += new_shop_list["quantity"]
    return shop_list



def launch():
    dishes = input("Введите названия блюд: ").split(", ")
    person_count = int(input("Введите количество человек: "))
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print(shop_list)

launch()

