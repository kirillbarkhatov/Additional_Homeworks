import requests
import json


def get_github_users(users:list) -> list:
    repos_list = []
    for user in users:
        url = f'https://api.github.com/users/{user}'
        user_data = requests.get(url).json()
        url = f'https://api.github.com/users/{user}/repos'
        response = requests.get(url)
        repos = response.json()
        user_repos = [repo['name'] for repo in repos]
        user_info = {"login": user_data['login'], "count of public repos": user_data['public_repos'], "repos": user_repos}
        repos_list.append(user_info)
    return json.dumps(repos_list, indent=4)






if __name__ == '__main__':
    users = ['kirillbarkhatov', 'skypro-008', 'Daanil21']
    result = get_github_users(users)
    print(result)