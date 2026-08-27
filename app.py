import streamlit as st

from meal_api import search_meals, get_meal_by_id, MealAPIError
from recipe_utils import parse_meal
from ui_components import display_recipe


st.set_page_config(
    page_title="Dishcovery",
    page_icon="🍽️",
    layout="centered",
)

st.title("🍽️ Dishcovery")
st.write("Search for a meal and discover a recipe.")


@st.cache_data
def get_cached_meal(meal_id):
    """Fetch and cache meal details to avoid repeated API requests."""
    return get_meal_by_id(meal_id)


# Search for meals using the user's query.
query = st.text_input(
    "Search for a meal",
    placeholder="Try chicken, pasta, curry..."
)

search_button = st.button("Search")

if search_button:
    if not query.strip():
        st.warning("Please enter a meal name.")
    else:
        try:
            meals = search_meals(query)

            if not meals:
                st.info("No meals found.")
                st.session_state.pop("search_results", None)
            else:
                st.session_state["search_results"] = meals

        except MealAPIError as error:
            # Remove old results so a failed search does not show stale data.
            st.session_state.pop("search_results", None)
            st.error(str(error))


if "search_results" in st.session_state:
    meals = st.session_state["search_results"]

    # Build a safe mapping between meal IDs and display names.
    meal_options = {
        meal.get("idMeal"): meal.get("strMeal", "Unknown meal")
        for meal in meals
        if isinstance(meal, dict) and meal.get("idMeal")
    }

    if not meal_options:
        st.warning("No valid meal results are available.")
    else:
        # Use meal IDs as selectbox values to avoid duplicate-name issues.
        selected_meal_id = st.selectbox(
            "Select a meal",
            options=list(meal_options.keys()),
            format_func=lambda meal_id: meal_options[meal_id]
        )

        try:
            # Retrieve the selected meal and parse the API data.
            full_meal = get_cached_meal(selected_meal_id)

            if full_meal is None:
                st.error("Could not retrieve this meal.")
            else:
                recipe = parse_meal(full_meal)

                if not recipe or not isinstance(recipe, dict):
                    st.warning("Could not parse recipe information.")
                else:
                    # Reuse the shared UI component instead of duplicating rendering logic.
                    display_recipe(recipe)

                    if recipe.get("source"):
                        st.link_button(
                            "View Original Recipe",
                            recipe["source"]
                        )

        except MealAPIError as error:
            st.error(str(error))