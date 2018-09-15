#!/usr/bin/python3

import os
import time
from typing import List, Any

from slackclient import SlackClient

print('Hey !')

SLACK_TOKEN = os.environ["SLACK_API_TOKEN"]

def connectToSlack(token: str) -> SlackClient:
    sc = SlackClient(token)
    if not sc.rtm_connect():
        raise Exception('Cannot connect to Slack API !')
    return sc

# Message example:
# [{'type': 'message', 'user': 'UCU8WQT0S', 'text': 'salut', 'client_msg_id': '7a93b31e-b08e-4497-b968-fa0c4bcf00af', 'team': 'TCU8WQSQJ', 'channel': 'DCVA9V607', 'event_ts': '1537010280.000100', 'ts': '1537010280.000100'}]

def processMessage(sc: SlackClient, raw: Any):
    message = raw['text']
    channel = raw['channel']

    sc.rtm_send_message(channel, message)


def listenMessages(sc: SlackClient) -> None:
    while True:
        rawMessages: List = sc.rtm_read()
        for raw in rawMessages:
            print(raw)
            if raw.get("type") and raw.get("type") == 'message':
                processMessage(sc, raw)
        time.sleep(1)


if __name__ == '__main__':
    sc = connectToSlack(SLACK_TOKEN)
    listenMessages(sc)
