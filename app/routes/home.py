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
    return render_template('display.html', platform=platform, info=info)