from CSTwitterAnalysis.twitter_collect.twitter_connection_setup import twitter_setup

def test_twitter_setup():
    assert isinstance(twitter_setup())
