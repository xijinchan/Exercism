"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients`.

    :param dish_name: str - containing the dish name.
    :param dish_ingredients: list - dish ingredients.
    :return: tuple - containing (dish_name, ingredient set).

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """
    de_dupe = set(dish_ingredients)
    
    output = (dish_name,de_dupe)

    return output

def check_drinks(drink_name, drink_ingredients):
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name`, based on `drink_ingredients`.

    :param drink_name: str - name of the drink.
    :param drink_ingredients: list - ingredients in the drink.
    :return: str - drink_name appended with "Mocktail" or "Cocktail".

    The function should return the name of the drink followed by "Mocktail" (non-alcoholic) and drink
    name followed by "Cocktail" (includes alcohol).

    """
    output = str(drink_name) + " Mocktail"

    for ingredient in drink_ingredients:
        if ingredient in ALCOHOLS:
            output = str(drink_name) + " Cocktail"
            break

    return output


def categorize_dish(dish_name, dish_ingredients):
    """Categorize `dish_name` based on `dish_ingredients`.

    :param dish_name: str - dish to be categorized.
    :param dish_ingredients: list - ingredients for the dish.
    :return: str - the dish name appended with ": <CATEGORY>".

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    `<CATEGORY>` can be any one of  (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`

    """
    if dish_ingredients.issubset(VEGAN): string_category = "VEGAN"
    if dish_ingredients.issubset(VEGETARIAN): string_category = "VEGETARIAN"
    if dish_ingredients.issubset(PALEO): string_category = "PALEO"
    if dish_ingredients.issubset(KETO): string_category = "KETO"
    if dish_ingredients.issubset(OMNIVORE): string_category = "OMNIVORE"

    print(string_category)

    output = dish_name + ": " + string_category
    print(output)
    
    return output


def tag_special_ingredients(dish):
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`.

    :param dish: tuple - of (dish name, list of dish ingredients).
    :return: tuple - containing (dish name, dish special ingredients).

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """
    dish_special_ingredients = set()

    cleaned_dish = clean_ingredients(dish[0], dish[1])

    for ingredient in cleaned_dish[1]:
        if ingredient in SPECIAL_INGREDIENTS:
            dish_special_ingredients.add(ingredient)

    output = (dish[0], dish_special_ingredients)
    print(output)

    return output

def compile_ingredients(dishes):
    """Create a master list of ingredients.

    :param dishes: list - of dish ingredient sets.
    :return: set - of ingredients compiled from `dishes`.

    This function should return a `set` of all ingredients from all listed dishes.
    """
    master_ingredients = set()

    for dish in dishes:
        master_ingredients = master_ingredients.union(dish)
        
    print(master_ingredients)

    return master_ingredients


def separate_appetizers(dishes, appetizers):
    """Determine which `dishes` are designated `appetizers` and remove them.

    :param dishes: list - of dish names.
    :param appetizers: list - of appetizer names.
    :return: list - of dish names that do not appear on appetizer list.

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """
    output = []

    for dish in dishes:
        if dish not in appetizers:
            output.append(dish)

    de_duped = set(output)
    return de_duped

def singleton_ingredients(dishes, intersection):
    """Determine which `dishes` have a singleton ingredient (an ingredient that only appears once across dishes).

    :param dishes: list - of ingredient sets.
    :param intersection: constant - can be one of `<CATEGORY>_INTERSECTIONS` constants imported from `sets_categories_data.py`.
    :return: set - containing singleton ingredients.

    Each dish is represented by a `set` of its ingredients.

    Each `<CATEGORY>_INTERSECTIONS` is an `intersection` of all dishes in the category. `<CATEGORY>` can be any one of:
        (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).

    The function should return a `set` of ingredients that only appear in a single dish.
    """
    unique = set()
    
    for dish in dishes:
        difference = dish.difference(intersection)
        for item in difference:
            unique.add(item)
    
    de_duped = set(unique)
    return de_duped
