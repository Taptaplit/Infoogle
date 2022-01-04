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

base_url = "https://api.github.com"
headers={'Authorization': f"token {os.environ.get('github_token')}"}

class GithubUser:
    def __init__(self, name):
        self.name = name

    def getUserInfo(self):
        response = requests.get(f"{base_url}/users/{self.name}", headers=headers)
        jsonRes = response.json()
        name = jsonRes["name"]
        avatar = jsonRes["avatar_url"]
        link = jsonRes["html_url"]
        followers = jsonRes["followers"]
        following = jsonRes["following"]
        bio = jsonRes["bio"]
        email = jsonRes["email"]
        
        return {'name': name, 'avatar': avatar, 'followers': followers, 'following': following, 'bio': bio, 'email': email, 'link': link}

    def getRepos(self):
        repoInfo = []
        response = requests.get(f"{base_url}/users/{self.name}/repos", headers=headers)
        jsonRes = response.json()
        for repo in jsonRes:
            name = repo["name"]
            link = repo["html_url"]
            language = repo["language"]
            stars = repo["stargazers_count"]
            forks = repo["forks"]
            repoInfo.append({'name': name, 'link': link, 'language': language, "stars": stars, "forks": forks})
        return repoInfo
    
    def getGists(self):
        return f"https://gists.github.com/{self.name}"
    