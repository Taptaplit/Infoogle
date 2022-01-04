"""
MIT License

Copyright (c) 2021 Taptaplit

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import os
import requests


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
    