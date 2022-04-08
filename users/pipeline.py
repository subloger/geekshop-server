
import requests
from social_core.exceptions import AuthForbidden
from users.models import ShopUser


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return

    access_token = response['access_token']
    version = '5.131'
    api_url = f'https://api.vk.com/method/users.get?fields=bdate%2Csex%2Cabout&access_token={access_token}&v={version}'

    resp = requests.get(api_url)
    if resp.status_code != 200:
        return
    data = resp.json()['response'][0]
    print(data)

    if data['sex'] in data:
        if data['sex'] == 2:
            user.shopuser.gender = ShopUser.MALE
        elif data['sex'] == 1:
            user.shopuser.gender = ShopUser.FEMALE
        else:
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')
    if data['about']:
        user.shopuser.about_me = data['about']
    user.save()
