# Food Calorie Counter

A web application that allows users to track their daily calorie intake using Django, Python, and an external API.

## Features

- User registration and authentication
- Search for foods and their calorie information
- Add foods to daily intake log
- View daily and weekly calorie summaries
- Set personalized calorie goals

## Technologies Used

- Django 4.2
- Python 3.9+
- Ninja API
- HTML/CSS
- Bootstrap 5

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/shresthacodes/food-calorie-counter.git
   cd food-calorie-counter
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   # On Mac,
   use source venv/bin/activate
   # On Windows,
   use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root and add your Nutritionix API credentials:
   ```
   
   NUTRITION_API_KEY=your_api_key
   ```


5. Start the development server:
   ```
   python manage.py runserver
   ```

6. Open your browser and navigate to `http://localhost:8000`

## Usage

1. Register a new account or log in
2. Search for foods using the search bar
3. Add foods to your daily intake log
4. View your calorie summary on the dashboard
5. Set and update your calorie goals in the profile section


