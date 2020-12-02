import os
import pytest
import unittest
import logging
import urllib.request
import ssl
from src.helpers.twitter_api_helpers import TwitterApiHelper
from src.helpers.read_and_write_text_file_helper import ReadAndWriteTextFileHelper

@pytest.mark.twitter_api_tests
class TwitterTests(unittest.TestCase):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    """
                Test post the tweet, retweet the same tweet, unretweet and finally delete the created tweet
    """

    def test_post_tweet_retweet_the_same_tweet_unretweet_and_finally_delete_the_tweet(self):

        #create object
        twitter_api_helper = TwitterApiHelper()

        # Make a new tweet with the text "We welcome you to MSD family :)"
        response_of_new_tweet = twitter_api_helper.post_new_tweet(status="We welcome you to MSD family :)")

        # get tweet id and twitter id from response_of_new_tweet
        tweet_id = response_of_new_tweet["id"]
        tweeter_id = response_of_new_tweet["user"]["id"]

        # retweet the same tweet
        response_of_retweet = twitter_api_helper.post_retweet(tweet_id=tweet_id)

        # get retweet_id,retweet_count,retweeter_id
        retweet_id = response_of_retweet["id"]
        retweet_count = response_of_retweet["retweet_count"]
        retweeter_id = response_of_retweet["user"]["id"]

        # check retweet count and it should be 1
        assert retweet_count == 1

        # check tweeter id and retweeter id are same
        assert tweeter_id == retweeter_id

        # unretweet the tweet
        response_of_unreweet = twitter_api_helper.unretweet(retweet_id=retweet_id)

        # Get retwitter id of the deleted retweet
        retweeter_id_of_deleted_retweet = response_of_unreweet["user"]["id"]

        # check correct retweet has been deleted
        assert retweeter_id == retweeter_id_of_deleted_retweet

        # check the retweet count should be 0 after unretweet
        response_of_tweet_details = twitter_api_helper.get_tweet_details_by_tweet_id(status_id=tweet_id)
        retweet_count_after_unretweet = response_of_tweet_details["retweet_count"]
        assert retweet_count_after_unretweet == 0

        # delete the tweet
        response_of_deleted_tweet = twitter_api_helper.delete_tweet(tweet_id=tweet_id)
        tweet_id_of_deleted_tweet = response_of_deleted_tweet["id"]

        # check correct tweet gets deleted
        assert tweet_id == tweet_id_of_deleted_tweet

    """
        Test Get twitter content, video, number of reweet and twitter id of the tweet and store it in a text file
    """

    def test_get_twitter_content_video_number_of_retweet_and_retwitter_id_of_the_tweet_and_store_it_in_text_file(self):

        #create objects
        twitter_api_helper = TwitterApiHelper()
        read_and_write_text_file_helper =ReadAndWriteTextFileHelper()

        # Get the tweet details by id
        response_of_tweet_details = twitter_api_helper.get_tweet_details_by_tweet_id(status_id="1257326183101980673")

        #get status from response_of_tweet_details
        status = response_of_tweet_details["full_text"]

        #get download link from response_of_tweet_details
        ssl._create_default_https_context = ssl._create_unverified_context
        url = response_of_tweet_details["extended_entities"]["media"][0]["video_info"]["variants"][0]["url"]
        #Download video from the status and save it in a folder
        urllib.request.urlretrieve(url, './msd/src/tests/videos/status_video.mp4')

        #create new text file
        file_name = "text_file"
        read_and_write_text_file_helper.create_and_add_data_in_txt_file(file_name=file_name,data=status)

        #get retweet count from the response_of_tweet_details and store it in a text file
        retweet_count = response_of_tweet_details["retweet_count"]
        read_and_write_text_file_helper.add_data_to_existing_file(file_name=file_name,data=str(retweet_count))

        #get retweet ids of the tweet
        retweet_ids_from_api = twitter_api_helper.get_retweet_ids_of_the_tweet(status_id="1257326183101980673")

        #write retweet ids into the text file
        for x in range(0,retweet_count,1):
            try:
                retweet_id =str(retweet_ids_from_api[x]["user"]["id"])
                read_and_write_text_file_helper.add_data_to_existing_file(file_name=file_name, data=retweet_id)
            except IndexError:
                break

    """
            Test Get twitter content, video, number of reweet and twitter id of the tweet and store it in a text file
    """

    def test_check_twitter_content_number_of_retweet_and_retwitter_id_of_the_tweet_with__data_stored_in_text_file(self):

        #create objects
        twitter_api_helper = TwitterApiHelper()
        read_and_write_text_file_helper =ReadAndWriteTextFileHelper()

        # Get the tweet details by id
        response_of_tweet_details = twitter_api_helper.get_tweet_details_by_tweet_id(status_id="1257326183101980673")

        #Get status text from response_of_tweet_details
        status = response_of_tweet_details["full_text"]

        #remove empty lines from the status
        status = os.linesep.join([s for s in status.splitlines() if s])

        #split the status into list using comma
        status=status.rsplit()

        #Read data from text file
        text_data_from_file,num_of_lines = read_and_write_text_file_helper.read_data_from_txt_file(file_name="text_file")

        #Get the status from the text file
        status_from_text_file = []
        for i in range(0,3, 1):
            #Remove spaces at the beginning and at the end of the string
            text_data_from_file[i] = text_data_from_file[i].strip()
            #add text to the list
            status_from_text_file.append(text_data_from_file[i])

        # remove empty lines
        while ('' in status_from_text_file):
            status_from_text_file.remove('')

        #concat the text into single line
        b=status_from_text_file[0]+" "+status_from_text_file[1]
        # split the text into list using comma
        status_from_text_file = b.rsplit()

        #iterate and check status from the response is same as the status in the text file
        for x in range(0,len(status_from_text_file),1):
            assert status_from_text_file[x]==status[x]

        #check retweet count is same in both text file and from the response
        retweet_count = str(response_of_tweet_details["retweet_count"])
        text_data_from_file[3]=text_data_from_file[3].strip()
        retweet_count = retweet_count.lstrip()
        assert text_data_from_file[3]==retweet_count

       #append retweet ids from the response into the list
        response_of_retweet_details = twitter_api_helper.get_retweet_ids_of_the_tweet(status_id="1257326183101980673")
        retweet_id_from_list = []
        for j in range(0, 199, 1):
            try:
                retweet_id = response_of_retweet_details[j]["user"]["id"]
                retweet_id_from_list.append(retweet_id)
            except IndexError:
                break

        #chech retweet ids are same in text file and from the response
        i = 0
        for k in range(4, num_of_lines, 1):
            text_data_from_file[k] = int(text_data_from_file[k])
            assert text_data_from_file[k] == retweet_id_from_list[i]
            i += 1