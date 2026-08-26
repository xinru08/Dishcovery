"""Streamlit components for displaying recipe information."""

import streamlit as st


def display_meal_info(recipe):
    """Display a meal image and its basic information."""
    if not isinstance(recipe, dict) or not recipe:
        st.warning("No recipe information is available.")
        return

    # Put the recipe's visual and identifying details first.
    image = recipe.get("image")
    if image:
        st.image(image, use_container_width=True)

    st.subheader(recipe.get("name") or "Recipe")

    basic_information = {
        "Category": recipe.get("category"),
        "Cuisine": recipe.get("area"),
    }
    available_information = {
        label: value
        for label, value in basic_information.items()
        if value
    }

    if available_information:
        st.write(available_information)


def display_ingredients(recipe):
    """Display the ingredients and their measurements."""
    st.subheader("Ingredients")

    # Keep each measurement beside the ingredient it describes.
    ingredients = recipe.get("ingredients", []) if isinstance(recipe, dict) else []
    if not ingredients:
        st.write("No ingredients available.")
        return

    for item in ingredients:
        if not isinstance(item, dict):
            continue

        ingredient = item.get("ingredient", "").strip()
        measure = item.get("measure", "").strip()
        if not ingredient:
            continue

        text = f"{measure} {ingredient}".strip()
        st.markdown(f"- {text}")


def display_instructions(recipe):
    """Display the cooking instructions."""
    st.subheader("Instructions")

    # The full preparation text stays together for easy reading.
    instructions = recipe.get("instructions") if isinstance(recipe, dict) else None
    st.write(instructions or "No instructions available.")


def display_recipe(recipe):
    """Display all available sections of recipe."""
    # Render the recipe in the same order a cook needs it.
    display_meal_info(recipe)
    display_ingredients(recipe)
    display_instructions(recipe)
