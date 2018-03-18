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
    import pyperclip
    import sys

    url = 'http://reddit.com'
    if len(sys.argv) > 1:
        url = sys.argv[1]

    access_key = config.access_key
    secret_keyword = config.secret_keyword

    response = screenshotlayer(access_key, secret_keyword, url, {})
    pyperclip.copy(response)
    print response
