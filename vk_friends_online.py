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
    list_of_users_ids = (vk_api.friends.getOnline(list_id=""))
    users_online_information = vk_api.users.get(user_ids=list_of_users_ids)
    return users_online_information


def output_friends_to_console(users_online_information):
    for friend in users_online_information:
        print(friend["first_name"], friend['last_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
