import external
from external import github

github_user = external.User.github("Taptaplit")
print(github_user.getUserInfo())
print(github_user.getRepos())
print(github_user.getGists())

stack_user = external.User.stackapps("stackoverflow", "Taptaplit10")
print(stack_user.getUserInfo())
print(stack_user.getQuestions())