# PreviewSiteBot
A Reddit bot that gets screenshots of websites

### Requirements

- Python 2.7
- PRAW
- [Screenshot Layer API](http://screenshotlayer.com)

### Setup
Define your environment variables (see `config.py` file) for the following variables:

- `CLIENT_ID`: Reddit app ID
- `CLIENT_SECRET`: Reddit app secret
- `ACCESS_KEY`: Access Key (Get from [Screenshot Layer API](http://screenshotlayer.com))
- `SECRET_KEYWORD`: Secret Keyword (Get from [Screenshot Layer API](http://screenshotlayer.com))

```python
# config.py
client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]

access_key = os.environ["ACCESS_KEY"]
secret_keyword = os.environ["SECRET_KEYWORD"]
```

### Run
```python
python previewSiteBot.py
```
