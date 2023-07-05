import requests

heads = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

r = open('settings.json', 'r')
r2 = r.read()

get_id = requests.post('https://users.roblox.com/v1/usernames/users', headers=heads, data=r2)
print(get_id.json()['data'][0].get('id'))

req2 = requests.post(f'https://www.opera.com/api/proxy/rolve/{get_id.json()["data"][0].get("id")}', headers=heads)
print(req2.text)
