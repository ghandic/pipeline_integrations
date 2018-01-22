from flask import Flask, request, make_response, Response
import os
import json
from slackclient import SlackClient

# Your app's Slack bot user token
SLACK_BOT_TOKEN = os.envirn["SLACK_BOT_TOKEN"]
SLACK_VERIFICATION_TOKEN = os.envirn["SLACK_VERIFICATION_TOKEN"]

# Slack client for Web API requests
slack_client = SlackClient(SLACK_BOT_TOKEN)

# Flask webserver for incoming traffic from Slack
app = Flask(__name__)

@app.route("/slack/message_actions", methods=["POST"])
def message_actions():

    # Parse the request payload
    form_json = json.loads(request.form["payload"])

    approver=form_json["user"]["name"]
    pipeline=form_json["callback_id"]

    # Check to see what the user's selection was and update the message
    selection = form_json["actions"][0]["value"]#["selected_options"][0]["value"]

    if selection == "yes":
        if pipeline=="data_move_dacc" and approver=="andrewchallis":
            message_text = "You have just approved the data move!"
            print("Do data move!")
        else:
            message_text = "You can't move the data you :horse:"
    else:
        message_text = "You have rejected the data move request"

    response = slack_client.api_call(
      "chat.update",
      channel=form_json["channel"]["id"],
      ts=form_json["message_ts"],
      text=message_text,
      attachments=[]
    )

    return make_response("", 200)



if __name__ == "__main__":
    app.run(port=3000)