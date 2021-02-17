# twitter-slack-bot
ActiveState tutorial to build a Twitter Slack Bot

# Install dependencies

All the dependencies are mentioned in the requirements.txt file. To install, run

pip install -r requirements.txt

# Run the Flask server

FLASK_APP=app.py FLASK_ENV=development flask run -p 3000

You can use Ngrok to expose your local server to the Internet.

ngrok http 3000
