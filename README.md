
#msd

## Python Setup
1. Install python 3.7.x version
2. pip install --user pipenv
3. create python virtual env: virtualenv venv
4. source virtualenv/bin/activate
5. Install the python modules from requirement.txt file

## Set path and credentials
1. Provide auth_token, consumer_key, consumer_secret, access_token, access_token_secret of the twitter user in src/helpers/authentication_helper.py
2. Provide path of the text file in src/helpers/read_and_write_text_file_helper.py

## Automation Framework
1. Framework Directory Structure:

```
src
    helpers : Reusable helper classes that perform actions on APIs
    tests : Test classes that define test methods for each use cases
```

## How to run tests
```
run tests:  pytest src/tests/twitter_test.py --self-contained-html --html=report.html

run tests in parallel using marker: pytest -v -m twitter_api_tests -n 4 --self-contained-html --html=report.html

run tests with re-run failed tests: pytest -v --reruns 2 -m twitter_api_tests -n 4 --self-contained-html --html=report.html
        (re-run the failed test twice before marking it as failure)

run individual test: pytest -v src/tests/twitter_test.py -k test_post_tweet_retweet_the_same_tweet_unretweet_and_finally_delete_the_tweet

run parallel test with json file : py.test -v --reruns 2 -m twitter_api_tests -n 4 --self-contained-html --html=contractor_web_tests.html --json=contractor_web.json

```
