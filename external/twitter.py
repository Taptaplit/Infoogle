import os
import requests


#### TAKE THIS OUT FOR PRODUCATION ####
from dotenv import load_dotenv
load_dotenv()
#######################################

headers = {'Authorization': f'Bearer {os.environ.get("twitter_bearer_token")}'}
base_url = "https://api.twitter.com"

class TwitterUser():
    def __init__(self, name):
        self.name = name
        self.id = None
    
    def getUserInfo(self):
        response = requests.get(f'{base_url}/2/users/by/username/{self.name}?user.fields=location,url,description,verified,profile_image_url,public_metrics', headers=headers)
        jsonRes = response.json()
        if jsonRes.get('data', '') != '':
            jsonRes = jsonRes['data']
            name = jsonRes['name']
            username = jsonRes['username']
            bio = jsonRes['description']
            verified = jsonRes['verified']
            location = jsonRes.get('location', '')
            followers = jsonRes['public_metrics']['followers_count']
            following = jsonRes['public_metrics']['following_count']
            tweets = jsonRes['public_metrics']['tweet_count']
            avatar = jsonRes['profile_image_url']
            self.id = jsonRes['id']
            
            return {'name': name, 'username': username, 'bio': bio, 'verified': verified, 'location': location, 'followers': followers, 'following': following, 'tweets': tweets, 'avatar': avatar}
        return {}

    def getTweets(self):
        tweets = []
        max_tweets = 0
        response = requests.get(f'{base_url}/2/users/{self.id}/tweets?exclude=replies', headers=headers)
        jsonRes = response.json()
        if jsonRes.get('data', '') != '':
            jsonRes = jsonRes['data']
            for tweet in jsonRes:
                if max_tweets < 5:
                    text = tweet['text']
                    tweets.append({ 'text': text })
                    max_tweets += 1
                else:
                    return tweets
                
        return tweets 
    