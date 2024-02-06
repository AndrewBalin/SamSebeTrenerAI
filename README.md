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