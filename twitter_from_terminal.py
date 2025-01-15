import tweepy
import sys
from dotenv import load_dotenv
import os

load_dotenv()


def verify_credentials(api_key, api_secret, access_token, access_token_secret):
    """
    Verify if the credentials are valid
    """
    auth = tweepy.OAuth1UserHandler(
        api_key, api_secret, access_token, access_token_secret
    )

    try:
        api = tweepy.API(auth)
        api.verify_credentials()
        print("✓ Credentials successfully verified!")
        return True
    except Exception as e:
        print(f"✗ Credential verification failed: {str(e)}")
        return False


def setup_twitter_client(api_key, api_secret, access_token, access_token_secret):
    """
    Setup Twitter API v2 client
    """
    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )
    return client


def post_tweet(client, text):
    """
    Post a tweet using Twitter API v2
    """
    try:
        response = client.create_tweet(text=text)
        print(f"✓ Tweet posted successfully!")
        return response
    except Exception as e:
        print(f"✗ Error posting tweet: {str(e)}")
        return None


if __name__ == "__main__":
    
    API_KEY = os.environ.get("API_KEY")
    API_SECRET = os.environ.get("API_SECRET")
    ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")



    # First verify credentials
    if not verify_credentials(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
        print("\nPlease check that:")
        print("1. All credentials are copied correctly (no extra spaces)")
        print("2. You're using Access Tokens (not Bearer Token)")
        print("3. The tokens were generated after setting Read+Write permissions")
        sys.exit(1)

    # If verification passed, setup client and post
    client = setup_twitter_client(
        API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
    )

    # Get tweet text from user input
    tweet_text = input("Enter your tweet: ")
    post_tweet(client, tweet_text)
