# Python Flask Application

This is a Python Flask application that uses the OpenAI GPT-3 model to create rations, training plans, and detect eating habits.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8
- pip

### Installing

1. Clone the repository
2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python app.py
```

## API Endpoints

The application has the following endpoints:

The Flask application has three main routes:

1. `/create_ration`: This route is used to create a ration. It accepts a POST request with a JSON body containing the necessary data and returns a generated ration.
```json
{
    "goal": "weight loss",
    "birth_date": "1990-01-01",
    "height": 180,
    "weight": 80,
    "gender": "male",
    "activity_level": "moderate",
    "equipment": "gym",
    "allergy": "peanuts",
    "training_days": 5,
    "liked_exercises": "running, swimming",
    "disliked_exercises": "cycling",
    "health_issues": "none"
}
```

2. `/create_training`: This route is used to create a training plan. It accepts a POST request with a JSON body containing the necessary data and returns a generated training plan.
```json
{
    "goal": "muscle gain",
    "level": "intermediate",
    "equipment": "dumbbells",
    "bottles": true,
    "training_days": "Monday, Wednesday, Friday",
    "liked_exercises": "bench press, deadlift",
    "disliked_exercises": "squats",
    "health_issues": "none"
}
```

3. `/detect_eat`: This route is used to detect eating habits. It accepts a POST request with a JSON body containing a URL and returns the detected eating habits.
```json
{
    "url": "https://example.com/image.jpg"
}
```

### POST /create_ration

This endpoint is used to create a ration. It accepts a JSON body with the necessary data and returns a generated ration.

### POST /create_training

This endpoint is used to create a training plan. It accepts a JSON body with the necessary data and returns a generated training plan.

### POST /detect_eat

This endpoint is used to detect eating habits. It accepts a JSON body with a URL and returns the detected eating habits.

## Built With

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [OpenAI GPT-3](https://openai.com/research/gpt-3/)

## Authors

- AndrewBalin

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details