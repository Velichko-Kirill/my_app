import requests
import requests_oauthlib

from demoproject.settings.base import *
import vk_api


def main():
    """ Получаем список имён и фамилий 5-ти случайных друзей """

    login, password = '89675926469', 'EddyDin1999'
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()

    count = 5
    friends = vk.friends.get(count=count, order='random', fields='nickname')

    if friends['items']:
        print(friends['items'])
        for i in range(count):
            print(friends['items'][i]['first_name'], friends['items'][i]['last_name'])



if __name__ == '__main__':
    main()