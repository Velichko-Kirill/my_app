import requests
import re

user_id = 382562174
req = requests.get(f'https://api.vk.com/method/friends.get?user_id={user_id}&count=5&fields=nickname&order=random&'
                 'access_token=75fa5a4b75fa5a4b75fa5a4b53758b445c775fa75fa5a4b2b6d8e79e0713fd2422c1db3&v=5.118')

#print(type(req), '\n', dir(req.content), '\n\n', req.text, '\n\n')
first_name_str = re.findall(r'(first_name":"[A-Za-z]+)', req.text)
last_name_str = re.findall(r'(last_name":"[A-Za-z]+)', req.text)

for i in range(len(first_name_str)):
    first_name_str[i] = re.sub(r'first_name\":"', '', first_name_str[i])
    last_name_str[i] = re.sub(r'last_name\":"', '', last_name_str[i])

for a, b in zip(first_name_str, last_name_str):
    print(a, b)