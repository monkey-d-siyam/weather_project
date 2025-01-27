# Weather Mama

Weather Mama is a Django-based web application that allows users to view the weather forecast for any city. Users can also create an account, log in, and save their favorite cities for quick access to the weather forecast.

## Features

- **User Authentication**: Sign up, log in, and log out.
- **Weather Forecast**: Get current weather information for any city.
- **User Profile**: Manage user profiles, change username and password.
- **Favorite Cities**: Save and view favorite cities for quick access.

## Technologies Used

- **Backend**: Django 5.1.4
- **Frontend**: HTML, CSS
- **Database**: MySQL
- **Weather API**: OpenWeatherMap API

## Installation
1. https://github.com/monkey-d-siyam/weather_project.git
2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate
3. Install Required Packages:
   pip install -r requirements.txt
4. Set up the Database:
   Update the DATABASES setting in weather_project/settings.py to connect to your MySQL database.
   Apply migrations to set up the database schema:
   python manage.py makemigrations forecast
   python manage.py migrate
5. Create a Superuser:
   python manage.py createsuperuser
6. Run the Development Server:
   python manage.py runserver

## Project Structure
- **forecast/models.py**: Defines the `UserProfile` and `City` models.
- **forecast/forms.py**: Contains the form definitions.
- **forecast/views.py**: Handles the views for authentication, profile management, and weather fetching.
- **forecast/urls.py**: Defines the URL patterns for the application.
- **forecast/templates/forecast**: Contains the HTML templates.
- **forecast/middleware.py**: Ensures user profiles are created upon login.
- **forecast/signals.py**: Handles the creation and saving of user profiles using Django signals.
- **static/**: Contains static files (CSS, JS, images).

## Configuration
### Weather API
1. **Sign up** for an API key at [OpenWeatherMap](https://openweathermap.org/api).
2. **Add the API Key** to your project's settings:
   ```python
   # weather_project/settings.py
   WEATHER_API_KEY = 'your_openweathermap_api_key'

## Usage
1. **Sign up** for an account or log in with an existing account.
2. **Enter a city name** in the search box to get the current weather forecast.
3. **Save favorite cities** for quick access.
4. **Manage your profile** by changing the username or password as needed.


## Contributing
1. **Fork the repository**.
2. **Create a new branch** (`git checkout -b feature-branch`).
3. **Make your changes**.
4. **Commit your changes** (`git commit -am 'Add new feature'`).
5. **Push to the branch** (`git push origin feature-branch`).
6. **Create a new Pull Request**.

## Contact
For any questions or suggestions, please feel free to contact me at [juborajahmed0213@gmail.com].

