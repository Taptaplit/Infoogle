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


import requests
import os

key = os.environ.get('stackapps_key')
base_url = 'https://api.stackexchange.com'

class StackUser():
    def __init__(self, app, user):
        self.app = str(app)
        self.user = str(user)
        self.user_id = []
    
    def getUserInfo(self):
        users = []
        response = requests.get(f"{base_url}/2.3/users?order=desc&sort=reputation&inname={self.user}&site={self.app}&key={key}")
        jsonRes = response.json()
        if jsonRes.get('items', '') != '':
            for user in jsonRes["items"]:
                self.user_id.append(user["user_id"])
                name = user['display_name']
                badges = user['badge_counts']
                reputation = user['reputation']
                location = user.get('location', '')
                link = user['link']
                avatar = user['profile_image']
                id = user['user_id']
                users.append({'name': name, 'badges': badges, 'reputation': reputation, 'location': location, 'link': link, 'avatar': avatar, 'id': id})
        return users

    def getQuestions(self):
        answers = []
        questions = []
        for id in self.user_id:
            response = requests.get(f"{base_url}/2.3/users/{id}/answers?order=desc&sort=activity&site={self.app}&key={key}")
            for answer in response.json()["items"]:
                owner = answer["owner"]["display_name"]
                owner_id = answer["owner"]["user_id"]
                accepted = answer["is_accepted"]
                score = answer["score"]
                answers.append({'owner': owner, 'score': score, 'accepted': accepted, 'owner_id': owner_id})
            response = requests.get(f"{base_url}/2.3/users/{id}/questions?order=desc&sort=activity&site={self.app}&key={key}")
            for question in response.json()["items"]:
                tags = question["tags"]
                owner = question["owner"]["display_name"]
                owner_id = question["owner"]["user_id"]
                answered = question["is_answered"]
                score = question["score"]
                title = question["title"]
                link = question["link"]
                questions.append({'owner': owner, 'score': score, 'answered': answered, 'tags': tags, 'title': title, 'link': link, 'owner_id': owner_id})
        return {'answers': answers, 'questions': questions}
    