import re

from user import User


# возвращает массив объектов друзей
def friends(api, userid):
    user_friends = api.friends.get(user_id=userid,
                                   order='hints', v=5.107)  # возвращает в том порядке, как расположены в разделе Мои
    return user_friends


userID = re.compile("vk.com\/id(\d*)")
user_name = re.compile("vk.com\/(\S+)")

login = input("login:")

password = input("password:")

my_user = User(login, password)
api = my_user.auth()

input_line = input("print user url")
try:
    user = userID.search(input_line).group(1)
except AttributeError:
    try:
        user = user_name.search(input_line).group(1)
    except AttributeError:
        print("bad url")
        user = "solodushkin_si"

id = api.users.get(user_ids=user, v=5.107)[0]["id"]
for el in api.users.get(user_ids=friends(api, id)["items"], v=5.107):
    print(el)
