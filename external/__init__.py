import external.github as github
import external.stackapps as stackapps
import external.twitter as twitter

class User(object):
    def github(name):
        return github.GithubUser(name)
    def stackapps(app, name):
        return stackapps.StackUser(app, name)
    def twitter(name):
        return twitter.TwitterUser(name)
    