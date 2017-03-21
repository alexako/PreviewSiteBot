import hmac
import hashlib
import urllib
import config


def screenshotlayer(access_key, secret_keyword, url, args):
    query = urllib.urlencode(dict(url=url, **args))
    secret_key = hashlib.md5('{}{}'.format(url, secret_keyword)).hexdigest()

    return "https://api.screenshotlayer.com/api/capture?access_key=%s&secret_key=%s&%s" \
            % (access_key, secret_key, query)

params = {
    'fullpage': '',
    'width': '',
    'viewport': '',
    'format': '',
    'css_url': '',
    'delay': '',
    'ttl': '',
    'force': '',
    'placeholder': '',
    'user_agent': '',
    'accept_lang': '',
    'export': ''
}

if __name__ == '__main__':
    access_key = config.access_key
    secret_keyword = config.secret_keyword
    url = 'http://reddit.com'

    print screenshotlayer(access_key, secret_keyword, url, params)
