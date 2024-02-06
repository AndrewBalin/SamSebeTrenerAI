from flask import Flask, request
from flask_ipfilter import IPFilter, Whitelist
from flask_cors import CORS

from dotenv import load_dotenv
import os

from source.RationCreator import RationCreator
from source.TrainingCreator import TrainingCreator
from source.EatDetector import EatDetector

load_dotenv()

rationCreator = RationCreator(key=os.getenv('CHAT_GPT_KEY'))
trainingCreator = TrainingCreator(key=os.getenv('CHAT_GPT_KEY'))
eatDetector = EatDetector(key=os.getenv('CHAT_GPT_KEY'))

app = Flask(__name__)
CORS(app)
ip_filter = IPFilter(app, ruleset=Whitelist())

ip_filter.ruleset.permit("127.0.0.1")


@app.route('/create_ration')
def create_ration():
    if request.method == 'POST':
        data = request.json
        prompt = rationCreator.get_prompt(**data)

        return rationCreator.generate(prompt), 200

    else:
        return 'Invalid request method', 400


@app.route('/create_training')
def create_training():
    if request.method == 'POST':
        data = request.json
        prompt = trainingCreator.get_prompt(**data)

        return trainingCreator.generate(prompt), 200

    else:
        return 'Invalid request method', 400


@app.route('/detect_eat')
def detect_eat():
    if request.method == 'POST':
        url = request.json['url']
        prompt = eatDetector.get_prompt()

        return eatDetector.generate(prompt, url), 200

    else:
        return 'Invalid request method', 400


if __name__ == '__main__':
    app.run()

