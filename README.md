# MealPlanner

MealPlanner is a web application that allows users to search for, save, and organize meal recipes. Using the Edamam Meal Planner API, users can easily discover nutritious meals and save them for later. It is a simple, user-friendly app designed to make meal planning easier and more enjoyable.

## Features

- **Meal Search**: Search for meals by entering food or meal names.
- **Meal Details**: View detailed information about each recipe, including ingredients, calories, and diet labels.
- **Save Meals**: Authenticated users can save meals to their account for easy access later.
- **Responsive Design**: The application is designed to work well on both desktop and mobile devices.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (Responsive Design)
- **API**: Edamam Meal Planner API
- **Database**: Django ORM (SQLite by default)

## Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.6 or higher
- Django 3.x or higher
- pip (Python package installer)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/mealplanner.git
cd mealplanner
```

### 2. Create a Virtual Environment (Recommended)

```bash
python3 -m venv venv
```

Activate the virtual environment:

- **On Windows**:
  ```bash
  venv\Scripts\activate
  ```

- **On MacOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up Environment Variables

In the project folder, create a `.env` file and add your Edamam API credentials. You can get your API keys by signing up at [Edamam](https://developer.edamam.com/).

```plaintext
EDAMAM_API_KEY=your_api_key_here
EDAMAM_APP_ID=your_app_id_here
```

### 5. Run Migrations

Make sure to apply any database migrations:

```bash
python manage.py migrate
```

### 6. Create a Superuser (Optional)

If you want to access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

### 7. Start the Development Server

Run the following command to start the server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser to view the application.

## Usage

- **Search Meals**: On the home page, use the search form to look for meals by entering food or meal names. The search results will display detailed information about each recipe, including the name, calories, diet labels, and a link to the full recipe.
  
- **Save Meals**: If you're logged in, you can save meals by clicking the "Save Meal" button. The meal will be added to your saved meals list for easy access later.

- **View Saved Meals**: Access your saved meals by navigating to the "Saved Meals" page.

### `mealplanner/`: Contains the main Django app, including settings, views, and models.
### `templates/`: Contains HTML files for different pages of the application.
### `static/`: Contains static files like CSS.
### `requirements.txt`: Contains a list of dependencies required to run the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Edamam API**: For providing the meal and recipe data.
- **Django**: For being an amazing web framework that makes development easier.
- **FontAwesome**: For their icon set used throughout the app.

---

Feel free to modify and adjust it based on any changes you might make to your project!
