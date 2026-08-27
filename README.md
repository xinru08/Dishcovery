# Dishcovery

Dishcovery is a recipe discovery application built by a six-person team for the AIPI 503 Python Bootcamp final project.

Users can search for meals and view recipe information retrieved from [TheMealDB API](https://www.themealdb.com/api.php).

## Minimum Viable Product

Dishcovery will:

- Search for meals by name
- Let the user select a search result
- Display the meal image, category, and cuisine
- Display ingredients and measurements
- Display cooking instructions
- Provide a command-line demo
- Provide a Streamlit web application
- Deploy the Streamlit application online

## Planned Project Structure

- `meal_api.py` — communicates with TheMealDB API
- `recipe_utils.py` — parses and formats recipe data
- `cli_demo.py` — provides the command-line interface
- `ui_components.py` — contains reusable Streamlit display functions
- `app.py` — runs the Streamlit application
- `requirements.txt` — lists required Python packages
- `CONTRIBUTING.md` — explains the team Git workflow

Team members will create the Python files through their assigned branches and pull requests.


## Prerequisites
- Python 3.10.0
- Git


## Local Setup

Clone the repository:

```bash
git clone https://github.com/xinru08/Dishcovery.git
cd Dishcovery
```

Create a virtual environment if one does not already exist:

```bash
python3 -m venv .venv
```

Activate it on macOS:

```bash
source .venv/bin/activate
# Windows: .venv/Scripts/activate.ps1
```

Install the dependencies:

```bash
python3 -m pip install -r requirements.txt
```

## Run the Command-Line Demo

```bash
python3 cli_demo.py
```

## Run the Streamlit App

```bash
python3 -m streamlit run app.py
```

## Team Development Workflow

1. Pull the latest version of `main`.
2. Create a branch for your assigned task.
3. Make and test your changes.
4. Commit your work with a clear message.
5. Push your branch to GitHub.
6. Open a pull request.
7. Ask at least one teammate to review it.
8. Merge only after review.

See [CONTRIBUTING.md](CONTRIBUTING.md) for complete instructions.

## Deployment

The live Streamlit application link will be added here after deployment.
