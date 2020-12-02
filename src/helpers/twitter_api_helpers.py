from http import HTTPStatus
import pytest
import logging
from src.helpers.api_helper import APIHelper
from  src.helpers.authentication_helper import AuthHelper


class TwitterApiHelper:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    APP_URL = "https://api.twitter.com/"


    """
       Get particular Tweet details by tweet id  : 1.1/statuses/show.json?id={id}&tweet_mode=extended
    """

    def get_tweet_details_by_tweet_id(
        self,
        status_id,
        auth_token=None,
        expected=HTTPStatus.OK,
    ):
        #create objects
        api_helper =APIHelper()
        auth_helper = AuthHelper()


        auth_token = auth_helper.auth_token
        method = "GET"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Bearer %s" % auth_token,
        }

        url = self.APP_URL+ "1.1/statuses/show.json?id=%s&tweet_mode=extended" % status_id

        #hit the api and get the response
        response = api_helper.api_response(method=method, url=url, headers=headers)

        self.logger.info("expected: %s response:%s" % (expected, response.status_code))
        if response.status_code == expected:
                response = response.json()
                self.logger.info("success: %s" % str(response))
        else:
                response = response.json()
                self.logger.info("failed: %s" % str(response))
                pytest.fail()
        return response



    """
           Get Retweet ids of the specific tweet: 1.1/statuses/retweets/%s.json
    """

    def get_retweet_ids_of_the_tweet(
            self,
            status_id,
            auth_token=None,
            expected=HTTPStatus.OK,
    ):
        # create objects
        api_helper = APIHelper()
        auth_helper = AuthHelper()
        auth_token = auth_helper.auth_token
        method = "GET"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Bearer %s" % auth_token,
        }
        payload = {
            "trim_user":True,
            "count": 100,
        }

        url = self.APP_URL + "1.1/statuses/retweets/%s.json?trim_user=True&count=100" % status_id

        # hit the api and get the response
        response = api_helper.api_response(method=method, url=url, headers=headers)

        self.logger.info("expected: %s response:%s" % (expected, response.status_code))
        if response.status_code == expected:
            response = response.json()
            self.logger.info("success: %s" % str(response))
        else:
            response = response.json()
            self.logger.info("failed: %s" % str(response))
            pytest.fail()
        return response


    """
            Post new tweet : 1.1/statuses/update.json
    """

    def post_new_tweet(
            self,
            status,
            expected=HTTPStatus.OK,
    ):
        # create objects
        api_helper = APIHelper()
        auth_helper = AuthHelper()
        auth_token = auth_helper.auth_token

        method = "POST"
        url = self.APP_URL + "1.1/statuses/update.json"
        params = {"status": status}

        # hit the api and get the response
        response = api_helper.api_response(method=method, url=url, auth_token=auth_helper.generate_oauth(),query=params)

        self.logger.info("expected: %s response:%s" % (expected, response.status_code))
        if response.status_code == expected:
            response = response.json()
            self.logger.info("success: %s" % str(response))
        else:
            response = response.json()
            self.logger.info("failed: %s" % str(response))
            pytest.fail()
        return response


    """
                  Post retweet : 1.1/statuses/retweet/{tweet_id}.json
    """

    def post_retweet(
            self,tweet_id,
            expected=HTTPStatus.OK,
    ):
        # create objects
        api_helper = APIHelper()
        auth_helper = AuthHelper()

        method = "POST"
        url = self.APP_URL + "1.1/statuses/retweet/%s.json" % tweet_id

        # hit the api and get the response
        response = api_helper.api_response(method=method, url=url, auth_token=auth_helper.generate_oauth())

        self.logger.info("expected: %s response:%s" % (expected, response.status_code))
        if response.status_code == expected:
            response = response.json()
            self.logger.info("success: %s" % str(response))
        else:
            response = response.json()
            self.logger.info("failed: %s" % str(response))
            pytest.fail()
        return response


    """
         Unreweet : 1.1/statuses/unretweet/{tweet_id}.json
    """

    def unretweet(
            self, retweet_id,
            expected=HTTPStatus.OK,
    ):
        # create objects
        api_helper = APIHelper()
        auth_helper = AuthHelper()

        method = "POST"
        url = self.APP_URL + "1.1/statuses/unretweet/%s.json" % retweet_id

        # hit the api and get the response
        response = api_helper.api_response(method=method, url=url, auth_token=auth_helper.generate_oauth())

        self.logger.info("expected: %s response:%s" % (expected, response.status_code))
        if response.status_code == expected:
            response = response.json()
            self.logger.info("success: %s" % str(response))
        else:
            response = response.json()
            self.logger.info("failed: %s" % str(response))
            pytest.fail()

        return response


    """
            Delete Tweet :1.1/statuses/destroy/{tweet_id}.json
    """

    def delete_tweet(
            self, tweet_id,
            expected=HTTPStatus.OK,
    ):
        # create objects
        api_helper = APIHelper()
        auth_helper = AuthHelper()

        method = "POST"
        url = self.APP_URL + "1.1/statuses/destroy/%s.json" % tweet_id

        # hit the api and get the response
        response = api_helper.api_response(method=method, url=url, auth_token=auth_helper.generate_oauth())

        self.logger.info("expected: %s response:%s" % (expected, response.status_code))
        if response.status_code == expected:
            response = response.json()
            self.logger.info("success: %s" % str(response))
        else:
            response = response.json()
            self.logger.info("failed: %s" % str(response))
            pytest.fail()

        return response