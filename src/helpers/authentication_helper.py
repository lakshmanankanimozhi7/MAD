import logging
from requests_oauthlib import OAuth1


class AuthHelper:
    logging.basicConfig(level=logging.INFO)

    auth_token = ""
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''

    def generate_oauth(self):
        auth = OAuth1(self.consumer_key, self.consumer_secret,
                      self.access_token, self.access_token_secret)
        return auth