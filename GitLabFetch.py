#GitLab HTTPS Link fetcher
#Made by Julien Galibois Sauvageau for Optel

import requests
import time
import json

print('Please enter your search terms.')
time.sleep(0.5)
print('This is usually a project number under one of the following formats.')
time.sleep(0.5)
print('P1234, p1234 or 1234')
search_terms = input('Search terms: ')
token = '' #Enter token here
gitlab_instance = '' #Enter URL here
url = gitlab_instance + 'api/v4/projects?private_token=' + token + '&search=' + search_terms 
resp = requests.get(url).json()

print('')
print('Results:')
print('')
for x in range(0, len(resp)):
    print('Serial Number: ' + [d["name"] for d in resp][x])
    print('Path on GitLab: ' + [d["name_with_namespace"] for d in resp][x])
    print('Last updated: ' + [d["last_activity_at"] for d in resp][x])
    http_url = [d["http_url_to_repo"] for d in resp][x]
    print('To download this system, the command to use is: ')
    print('git clone https://oauth2:' + token + '@' + http_url[8:])
    print('')
    print('')
