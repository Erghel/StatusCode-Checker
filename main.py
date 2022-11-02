import requests

site = input('Enter website: ').replace('https://', '').replace('http://', '')
print('You enter this site: ' + site)
req = requests.get('https://' + site)

print(req.status_code)
