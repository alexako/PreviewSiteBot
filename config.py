import os

client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]
username = ""
password = ""
subreddit = "all"
user_agent = "PreviewSiteBot v1.2 for /r/%s, by /u/kludgebot" \
            % (subreddit)

#Keywords to trigger the bot
keywords = ["!preview", "!previewbot", "!previewsite", "!previewsitebot"]

#Screenshotlayer credentials - http://screenshotlayer.com
access_key = os.environ["ACCESS_KEY"]
secret_keyword = os.environ["SECRET_KEYWORD"]

