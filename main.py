import requests

response = requests.get("https://api.github.com/users/momo1000")
my_projects = [response.json()]

print(my_projects)
for project in my_projects:
    print(f'Project Name:{project["login"]} ProjectUrl: {project["gists_url"]}')