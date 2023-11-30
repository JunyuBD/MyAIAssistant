from pprint import pprint
import json
from openai import OpenAI
import time
import lark_oapi as lark
from lark_oapi.api.docx.v1 import *
from lark_oapi.api.drive.v1 import *
from flask import Flask, request, jsonify, redirect, Response
from bot import *


app = Flask(__name__)

@app.route("/bot/callback", methods=["POST"])
def bot_callback():
    # print(request.headers)
    if 'challenge' in request.json:
        return json.dumps({
            "challenge": request.json['challenge']
    })

    print(request.json)
    print(request.json['event']['sender']['sender_id']['open_id'])
    user_open_id = request.json['event']['sender']['sender_id']['open_id']
    default_respond = json.dumps({
        "success": "cool"
    })

if __name__ == '__main__':
    app.run(debug=True, port=80)