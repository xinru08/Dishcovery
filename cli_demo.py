"""Command-line demo for the Dishcovery recipe app."""

from meal_api import MealAPIError, get_meal_by_id, search_meals
from recipe_utils import parse_meal


def display_search_results(meals):
    """
    Print numbered meal search results.

    Parameters: 
        meals (list): A list of meal dictionaries returned by TheMealDB API.
    """
    print("\nSearch results:")

    # Print each meal with its index, name, category, and area
    for index, meal in enumerate(meals, start=1):
        name = meal.get("strMeal", "Unknown meal")
        category = meal.get("strCategory", "Unknown category")
        area = meal.get("strArea", "Unknown cuisine")
        print(f"{index}. {name} ({category}, {area})")


def get_selection(number_of_results):
    """
    Ask the user to choose a result and return its zero-based index.
    
    Parameters: 
        number_of_results (int): The number of available search results.

    Returns:
        int: The zero-based index of the selected recipe.
    """
    while True:
        choice = input(
            f"\nSelect a recipe (1-{number_of_results}) or 'q' to quit: "
        ).strip()

        if choice.lower() == "q":
            return None

        # Validate that the input is a number and within the valid range
        # Keep the demo running without crashing on invalid input
        try:
            choice_number = int(choice)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if 1 <= choice_number <= number_of_results:
            return choice_number - 1

        print(f"Please enter a number from 1 to {number_of_results}.")


def print_recipe(recipe):
    """
    Print a parsed recipe in a readable format.
    
    Parameters:
        recipe (dict): A parsed recipe dictionary containing recipe details.
    """
    print("\n" + "=" * 60)
    print(recipe.get("name") or "Unknown Recipe")
    print("=" * 60)

    print(f"Category: {recipe.get('category') or 'N/A'}")
    print(f"Cuisine:  {recipe.get('area') or 'N/A'}")

    print("\nIngredients:")
    ingredients = recipe.get("ingredients", [])
    if ingredients:
        for item in ingredients:
            ingredient = item.get("ingredient", "")
            measure = item.get("measure", "")
            if measure:
                print(f"- {measure} {ingredient}")
            else:
                print(f"- {ingredient}")
    else:
        print("- No ingredients available")

    print("\nInstructions:")
    print(recipe.get("instructions") or "No instructions available.")

    if recipe.get("source"):
        print(f"\nSource: {recipe['source']}")

    if recipe.get("image"):
        print(f"Image:  {recipe['image']}")

    print("=" * 60)


def main():
    """
    Run the Dishcovery command-line demo.
    """
    print("Welcome to Dishcovery!")

    while True:
        search_term = input("Enter a meal to search for: ").strip()

        meals = search_meals(search_term)
        if not meals:
            print("No recipes found.")

            choice = input("Would you like to search again? (y/n): ").strip().lower()

            if choice == "y":
                continue

            print("Goodbye!")
            return

        display_search_results(meals)

        selected_index = get_selection(len(meals))

        if selected_index is None:
            print("Goodbye!")
            return

        meal_id = meals[selected_index].get("idMeal")
        selected_meal = get_meal_by_id(meal_id)

        recipe = parse_meal(selected_meal)

        # Check if the recipe is a valid dictionary
        if not isinstance(recipe, dict):
            print(recipe)

            choice = input("Would you like to search again? (y/n): ").strip().lower()

            if choice == "y":
                continue

            print("Goodbye!")
            return

        print_recipe(recipe)

        choice = input("\nWould you like to search for another recipe? (y/n): ").strip().lower()

        if choice != "y":
            print("Goodbye!")
            return


if __name__ == "__main__":
    main()