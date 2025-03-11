from dotenv import load_dotenv
import requests
import os

load_dotenv()

# Replace with your Bearer Token from Twitter Developer Portal
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

def get_user_id(username):
    url = f"https://api.twitter.com/2/users/by/username/{username}"
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"User lookup failed: {response.status_code} {response.text}")
    
    return response.json()['data']['id']

def get_user_tweets(user_id, max_results=10):
    url = f"https://api.twitter.com/2/users/{user_id}/tweets"
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    params = {
        "max_results": max_results,
        "tweet.fields": "created_at",
        "exclude": "retweets,replies"  # Optional: remove this line to include all tweets
    }
    
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(f"Tweets retrieval failed: {response.status_code} {response.text}")
    
    return response.json()

if __name__ == "__main__":
    # Get username input
    username = input("Enter Twitter username: ").strip().replace('@', '')
    
    try:
        # Get user ID
        user_id = get_user_id(username)
        print(f"User ID for @{username}: {user_id}")
        
        # Get tweets
        tweets = get_user_tweets(user_id, max_results=10)
        
        # Display tweets
        print(f"\nRecent tweets from @{username}:")
        for tweet in tweets['data']:
            print(f"{tweet['created_at']}: {tweet['text']}\n")
            
    except Exception as e:
        print(f"Error: {e}")