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
    my_id_number = [id_number['uid'] for id_number in vk_api.users.get(user_id=0)]
    list_of_online_id_numbers = vk_api.friends.getOnline(user_id=my_id_number)
    dict_of_info_firends_online = []
    for friend_id_number in list_of_online_id_numbers:
        dict_of_info_firends_online.append(vk_api.users.get(user_id=friend_id_number))
    return dict_of_info_firends_online


def output_friends_to_console(list_of_friends_online):
    for friend in list_of_friends_online:
        first_name = ("".join(friend_personal_info['first_name'] for friend_personal_info in friend))
        second_name = ("".join(friend_personal_info['last_name'] for friend_personal_info in friend))
        print(first_name, second_name)


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
