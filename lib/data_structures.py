spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food.get("name") for food in spicy_foods ]
    
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food.get("heat_level") > 5 ]

def print_spicy_foods(spicy_foods):
    print_list = [food.get("name")+" ("+food.get("cuisine")+") | Heat Level: "+"🌶"*food.get("heat_level") for food in spicy_foods]
    print(*print_list, sep = "\n")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    cuis_list = [food for food in spicy_foods if food.get("cuisine") == cuisine]
    return cuis_list[0]

def print_spiciest_foods(spicy_foods):
    print_list = [food.get("name")+" ("+food.get("cuisine")+") | Heat Level: "+"🌶"*food.get("heat_level") for food in spicy_foods if food.get("heat_level") > 5]
    print(*print_list, sep = "\n")


def get_average_heat_level(spicy_foods):
    heat_levels = [food.get("heat_level") for food in spicy_foods]
    
    total = 0
    for i in range(0,len(heat_levels)):
        total += heat_levels[i]

    average = total/len(heat_levels)

    return int(average)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

