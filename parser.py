import requests
import json

ID = 'ID_GROUP' #ID группы
TOKEN = 'TOKEN' #Токен
COUNT = '1000'
ALL = '100000' #Количество подписчиков группы
FIELDS = 'sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200, ' \
         'photo_400_orig, photo_max, photo_max_orig, online, online_mobile, lists, ' \
         'domain, has_mobile, contacts, connections, site, education, universities, schools,' \
         'can_post, can_see_all_posts, can_see_audio, can_write_private_message, status, ' \
         'last_seen'

def url(ID,TOKEN,FIELDS,OFFSET,COUNT):
    URL = 'https://api.vk.com/method/groups.getMembers.json?' \
            'group_id=%s' \
            '&access_token=%s' \
            '&fields=%s' \
            '&offset=%s' \
            '&count=%s' \
            '&v=5.95' % (ID,TOKEN,FIELDS,OFFSET,COUNT)
    return URL

users_all = []
with open( 'user.txt', 'a', encoding='utf8') as file:
    for i in range(0,int(ALL),1000):
        get = requests.get(url(ID, TOKEN, FIELDS, i, COUNT))
        json = get.json()['response']['items']
        for user in json:
            users_all.append(user)
            file.write( str(user) + '\n' )
        print (len(users_all))
