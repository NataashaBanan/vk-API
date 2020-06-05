import vk


class User(object):
    """VK User"""

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.id = ''

    # аторизирует юзера
    def auth(self):
        session = vk.AuthSession(app_id='5340228', user_login=self.login,
                                 user_password=self.password)
        api = vk.API(session)
        return api
