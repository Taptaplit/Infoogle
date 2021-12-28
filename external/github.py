import os
import requests

base_url = "https://api.github.com"
headers={'Authorization': os.environ.get('github_token')}


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
    