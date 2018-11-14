#test du module twitter_connection_setup.py

import pytest
from tweet_collect.twitter_connection_setup import twitter_setup

def test_twitter_setup():
    assert twitter_setup() != None

