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


from flask import Blueprint, render_template, request
import importlib.util, os

def module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

external = module_from_file("foo", f"{os.path.join(os.path.dirname(__file__), '../..')}/external/__init__.py")

home = Blueprint('home', __name__)  

@home.route('/', methods=['GET'])
def homePage():
    return render_template('index.html')

@home.route('/', methods=['POST'])
def getUser():
    username = request.form['username']
    platform = request.form['platform']
    if platform == 'github':
        user = external.User.github(username)
        info = user.getUserInfo()
        repos = user.getRepos()
        mainLang = 0
        stars = 0
        forks = 0
        lang = []
        for repo in repos:
            if repo["language"] not in lang and repo["language"] != None:
                lang.append(repo["language"])
                mainLang += 1
            stars += repo["stars"]
            forks += repo["forks"]            
        return render_template('display.html', platform=platform, info=info, repos=repos, mainLang=mainLang, totalForks=forks, totalStars=stars)
    elif platform == "stackoverflow" or platform == "askubuntu" or platform == "stackexchange" or platform == "mathematics":
        user = external.User.stackapps(platform, username)
        info = user.getUserInfo()
        questions = user.getQuestions()
        return render_template('display.html', platform=platform, info=info, questions=questions)
    elif platform == "twitter":
        user = external.User.twitter(username)
        info = user.getUserInfo()
        tweets = user.getTweets()
        return render_template('display.html', platform=platform, user=info, tweets=tweets)
    return "404"