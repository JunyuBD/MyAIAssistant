import json

import requests


def bot_mentioned_in_group(event, bot_open_id):
    print(f"message {event['message']}")
    print(f"bot open id: {bot_open_id}")
    if 'mentions' not in event['message']:
        return False

    if bot_open_id != event['message']['mentions'][0]['id']['open_id']:
        return False

    return True


def reply_msg(app_id, message_id, msg):
    url = f"https://open.feishu.cn/open-apis/im/v1/messages/{message_id}/reply"
    msgContent = {
        "text": msg,
    }
    req = {
        "msg_type": "text",
        "content": json.dumps(msgContent)
    }
    payload = json.dumps(req)
    access_token = get_tenant_access_token(app_id)
    headers = {
        'Authorization': f'Bearer {access_token}',  # your access token
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.headers['X-Tt-Logid'])  # for debug or oncall
    print(response.content)  # Print Response


def get_tenant_access_token(app_id):
    url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal'
    req = {
        "app_id": app_id,
        "app_secret": CONFIG[app_id]
    }
    payload = json.dumps(req)
    response = requests.request("POST", url, data=payload)
    content = json.loads(response.content)
    print(content["tenant_access_token"])  # Print Response
    return content["tenant_access_token"]