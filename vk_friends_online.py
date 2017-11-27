import vk
import getpass

APP_ID = 6269570


def get_user_login():
    login = input("Enter your username or phone number: ", )
    return login


def get_user_password():
    password = getpass.getpass()
    return password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope="friends")

    vk_api = vk.API(session)
    my_id = [id['uid'] for id in vk_api.users.get(user_id=0)]
    list_of_online_ids = vk_api.friends.getOnline(user_id=my_id)
    dict_of_info_firends_online = []
    for friend_id in list_of_online_ids:
        dict_of_info_firends_online.append(vk_api.users.get(user_id=friend_id))
    return dict_of_info_firends_online


def output_friends_to_console(friends_online):
    for friend in friends_online:
        name = ("".join(data['first_name'] for data in friend))
        surname = ("".join(data['last_name'] for data in friend))
        print(name, surname)


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
