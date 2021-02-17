from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from flask import Flask, request
import twitter

flask_app = Flask(__name__)
app = App(
  token="...",
  signing_secret="..."
)
api = twitter.Api(
  consumer_key='...',
  consumer_secret='...',
  access_token_key='...',
  access_token_secret='...'
)
handler = SlackRequestHandler(app)

@app.event("app_mention")
def event_test(body, say, logger):
  result = body["event"]["text"].split("Post this -")
  if len(result) == 2:
    status = api.PostUpdate(result[1].strip())
    link = "https://twitter.com/"+status.user.screen_name+"/status/"+str(status.id)
    say("Here's your tweet: " + link)

@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

# pip install -r requirements.txt
# export SLACK_SIGNING_SECRET=***
# export SLACK_BOT_TOKEN=xoxb-***
# FLASK_APP=app.py FLASK_ENV=development flask run -p 3000
# ngrok http 3000
