import streamlit as st

from meal_api import search_meals, get_meal_by_id, MealAPIError
from recipe_utils import parse_meal


st.set_page_config(
    page_title="Dishcovery",
    page_icon="🍽️",
    layout="centered",
)

st.title("🍽️ Dishcovery")
st.write("Search for a meal and discover a recipe.")


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
            st.error(str(error))


if "search_results" in st.session_state:
    meals = st.session_state["search_results"]

    meal_names = [meal["strMeal"] for meal in meals]

    selected_name = st.selectbox(
        "Select a meal",
        meal_names
    )

    selected_meal = next(
        meal
        for meal in meals
        if meal["strMeal"] == selected_name
    )

    meal_id = selected_meal["idMeal"]

    try:
        full_meal = get_meal_by_id(meal_id)

        if full_meal is None:
            st.error("Could not retrieve this meal.")
            recipe = None
        else:
            recipe = parse_meal(full_meal)

    except MealAPIError as error:
        st.error(str(error))
        recipe = None


    if recipe:
        st.header(recipe["name"])

        if recipe["image"]:
            st.image(
                recipe["image"],
                use_container_width=True
            )

        st.write(f"**Category:** {recipe['category']}")
        st.write(f"**Cuisine:** {recipe['area']}")

        st.subheader("Ingredients")

        for item in recipe["ingredients"]:
            measure = item["measure"]
            ingredient = item["ingredient"]

            if measure:
                st.write(f"- {measure} {ingredient}")
            else:
                st.write(f"- {ingredient}")

        st.subheader("Instructions")
        st.write(recipe["instructions"])

        if recipe["source"]:
            st.link_button(
                "View Original Recipe",
                recipe["source"]
            )