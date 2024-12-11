"""
Write a program that reads recipes from a json file.
The recipe contains a list of ingredients.
The program should also read a second json file that contains a list of products available in stores.
The program should ask the user which dish he wants to cook and print on the screen the stores where the user needs to go to collect the ingredients for that dish.
The program should try to make the user go to as few stores as possible to save time and money.
If the ingredients for the selected dish cannot be found, it should tell the user that the dish cannot be prepared in that city.
"""

import json
from itertools import combinations  # to find all possible combinations of stores

def find_minimum_stores(recipe_name, recipes, markets):
    recipe = next((r for r in recipes if r["name"].lower() == recipe_name.lower()), None)
    if not recipe:
        return None

    required_ingredients = set(recipe["ingredients"])
    market_items = {market["name"]: set(market["items"]) for market in markets}

    all_stores = list(market_items.keys())
    for r in range(1, len(all_stores) + 1):
        for store_combination in combinations(all_stores, r):
            combined_items = set()
            for store in store_combination:
                combined_items.update(market_items[store])
            if required_ingredients.issubset(combined_items):
                return list(store_combination)

    return None


def get_dish_choice(recipes):
    print("Available dishes:")
    for recipe in recipes:
        print(f"- {recipe['name']}")
    while True:
        dish = input("What dish would you like to cook? ").strip()
        if any(r["name"].lower() == dish.lower() for r in recipes):
            return dish
        print("Sorry, that's not a valid choice. Please try again.")


def load_json_file(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: File {file_path} is not a valid JSON.")
        exit(1)


def main():
    recipes = load_json_file("recipes.json")
    markets = load_json_file("markets.json")

    if not recipes or not markets:
        print("Error: Recipes or market data is missing.")
        return

    dish = get_dish_choice(recipes)
    stores = find_minimum_stores(dish, recipes, markets)

    if stores:
        print(f"To cook {dish}, you need to visit the following stores:")
        for store in stores:
            print(f"- {store}")
    else:
        print(f"Sorry, the ingredients for {dish} are not available in this city.")



if __name__ == "__main__":
    main()