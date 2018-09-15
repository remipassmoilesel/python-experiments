# Installation

## Token

- https://api.slack.com/ > Applications > Create a new app
- Bot users > Create bot users
- Install app > Builder > Install app to workspace

Then copy Bot user oauth access token to config.sh file:

    $ source ./slack_token.sh
    $ ./slack-client.py