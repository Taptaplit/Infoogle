import requests

base_url = 'https://api.stackexchange.com'

class StackUser():
    def __init__(self, app, user):
        self.app = str(app)
        self.user = str(user)
        self.user_id = []
    
    def getUserInfo(self):
        users = []
        response = requests.get(f"{base_url}/2.3/users?order=desc&sort=reputation&inname={self.user}&site={self.app}")
        jsonRes = response.json()
        for user in jsonRes["items"]:
            self.user_id.append(user["user_id"])
            name = user['display_name']
            badges = user['badge_counts']
            reputation = user['reputation']
            location = user.get('location', '')
            link = user['link']
            avatar = user['profile_image']
            users.append({'name': name, 'badges': badges, 'reputation': reputation, 'location': location, 'link': link, 'avatar': avatar})
        return users

    def getQuestions(self):
        answers = []
        questions = []
        for id in self.user_id:
            response = requests.get(f"{base_url}/2.3/users/{id}/answers?order=desc&sort=activity&site={self.app}")
            for answer in response.json()["items"]:
                owner = answer["owner"]["display_name"]
                accepted = answer["is_accepted"]
                score = answer["score"]
                answers.append({'owner': owner, 'score': score, 'accepted': accepted})
            response = requests.get(f"{base_url}/2.3/users/{id}/questions?order=desc&sort=activity&site={self.app}")
            for question in response.json()["items"]:
                tags = question["tags"]
                owner = question["owner"]["display_name"]
                answered = question["is_answered"]
                score = question["score"]
                title = question["title"]
                link = question["link"]
                questions.append({'owner': owner, 'score': score, 'answered': answered, 'tags': tags, 'title': title, 'link': link})
        return {'answers': answers, 'questions': questions}
    