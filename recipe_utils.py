

# Extract populated ingredients from strIngredient1-strIngredient20
# Match each ingredient with strMeasure1-strMeasure20
# Build and return a clean recipe dictionary


def parse_meal(meal):
    """Parse raw meal data into a clean recipe dictionary."""

    # data validation
    # raw meal data is a dictionary
    if not isinstance(meal, dict) or not meal:
        return None


    # extract relative fields
    meal_id = meal.get("idMeal")
    name = meal.get("strMeal")
    category = meal.get("strCategory")
    area = meal.get("strArea")
    country = meal.get("strCountry")
    instructions = meal.get("strInstructions")
    image = meal.get("strMealThumb")
    source = meal.get("strSource")

    # pair ingredients and measurements together

    # create a list for ingredients
    # go through each ingredient and associated measurement and pair them together
    ingredients = []

    for i in range(1, 21):
        ingredient = meal.get(f"strIngredient{i}")
        measure = meal.get(f"strMeasure{i}")

        if ingredient and ingredient.strip(): # accounts for empty ingredients
            ingredients.append(
                {
                    "ingredient": ingredient.strip(),
                    "measure": measure.strip() if measure else "", # accounts of empty measurements 
                }
            )

    # return a clean dictionary

    recipe = {
        "id": meal_id,
        "name": name,
        "category": category,
        "area": area,
        "country": country,
        "instructions": instructions,
        "ingredients": ingredients,
        "image": image,
        "source": source,
    }

    return recipe


# ============ TEST - commented out ====================
# if __name__ == "__main__":
#     sample_meal = {
#         "idMeal": "12345",
#         "strMeal": "Test Meal",
#         "strCategory": "Dinner",
#         "strArea": None,
#         "strCountry": "USA",
#         "strInstructions": "Cook everything.",
#         "strMealThumb": "https://example.com/image.jpg",
#         "strSource": "https://example.com",

#         "strIngredient1": "Chicken",
#         "strMeasure1": "2 breasts",

#         "strIngredient2": "Salt",
#         "strMeasure2": "",

#         "strIngredient3": "",
#         "strMeasure3": "",

#         "strIngredient4": "Pepper",
#         "strMeasure4": "1 tsp",
#     }

# print(parse_meal(sample_meal))
# print(parse_meal(None))
# print(parse_meal({}))