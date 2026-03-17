python
from flask import Flask, request
import requests

app = Flask(__name__)

VERIFY_TOKEN = "makewebhook"
MAKE_WEBHOOK = "https://hook.us2.make.com/eliuiuvpy6xv8kvovxlckdk5gwowh"

@app.route("/webhook", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200
    return "Forbidden", 403

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    try:
        requests.post(MAKE_WEBHOOK, json=data, timeout=5)
    except:
        pass
    return "OK", 200

if __name__ == "__main__":
    app.run()
