"""Functions for retrieving meal data from TheMealDB API."""

import requests


BASE_URL = "https://www.themealdb.com/api/json/v1/1"
REQUEST_TIMEOUT = 10


class MealAPIError(Exception):
    """Raised when meal information cannot be retrieved."""


def _get_json(endpoint, params):
    """Request one API endpoint and return its JSON data."""

    try:
        response = requests.get(
            f"{BASE_URL}/{endpoint}",
            params=params,
            timeout=REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        data = response.json()

    except (requests.RequestException, ValueError) as error:
        raise MealAPIError(
            "Unable to retrieve meal data from TheMealDB."
        ) from error

    if not isinstance(data, dict):
        raise MealAPIError("TheMealDB returned unexpected data.")

    return data


def search_meals(query):
    """Return meals whose names match the search query."""

    if query is None:
        return []

    query = query.strip()

    if not query:
        return []

    data = _get_json(
        "search.php",
        {"s": query},
    )

    return data.get("meals") or []


def get_meal_by_id(meal_id):
    """Return the meal matching an ID, or None if it is not found."""

    if meal_id is None:
        return None

    meal_id = str(meal_id).strip()

    if not meal_id:
        return None

    data = _get_json(
        "lookup.php",
        {"i": meal_id},
    )

    meals = data.get("meals") or []

    return meals[0] if meals else None

if __name__ == "__main__":
    query = input("Enter a meal name to search: ").strip()

    try:
        meals = search_meals(query)
        print(f"Found {len(meals)} matching meal(s).")

        if meals:
            first_meal = get_meal_by_id(meals[0]["idMeal"])
            print(f"First result: {first_meal['strMeal']}")

    except MealAPIError as error:
        print(error)
