"""
Write a program that reads recipes from a json file.
The recipe contains a list of ingredients.
The program should also read a second json file that contains a list of products available in stores.
The program should ask the user which dish he wants to cook and print on the screen the stores where the user needs to go to collect the ingredients for that dish.
The program should try to make the user go to as few stores as possible to save time and money.
If the ingredients for the selected dish cannot be found, it should tell the user that the dish cannot be prepared in that city.
"""

import json

def find_stores_for_recipe(recipe_name, recipes, markets):
    recipe = next((r for r in recipes if r["name"] == recipe_name), None)
    if not recipe:
        return None

    required_stores = set()
    for ingredient in recipe["ingredients"]:
        found_in_store = False
        for market in markets:
            if ingredient in market["items"]:
                required_stores.add(market["name"])
                found_in_store = True
                break
        if not found_in_store:
            return None

    return list(required_stores)


def main():
    with open("recipes.json", "r") as f:
        recipes = json.load(f)

    with open("markets.json", "r") as f:
        markets = json.load(f)

    dish = input("What dish would you like to cook? ")

    stores = find_stores_for_recipe(dish, recipes, markets)

    if stores:
        print(f"To cook the {dish}, you need to visit the following stores:")
        for store in stores:
            print(f"- {store}")
    else:
        print(f"Sorry, the ingredients for {dish} are not available in this city.")


if __name__ == "__main__":
    main()