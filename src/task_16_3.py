import requests
import json


def get_github_repos(user):
    repos_list = []
    url = f'https://api.github.com/users/{user}/repos'
    response = requests.get(url)
    repos = response.json()
    user_repos = [repo['name'] for repo in repos]
    return user_repos






if __name__ == '__main__':
    repos = get_github_repos('kirillbarkhatov')
    print(repos)