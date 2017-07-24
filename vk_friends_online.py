import vk
import getpass


APP_ID = 6121431


def get_user_login():
    return input("Input your login:")


def get_user_password():
    return getpass.unix_getpass("Input your password: ")


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope="friends"
    )
    api = vk.API(session)
    friends_online_ids = api.friends.getOnline()
    return api.friends.get(list_id=friends_online_ids, fields="first_name, last_name")


def output_friends_to_console(friends_online):
    if friends_online:
        print("{0} friends online:".format(len(friends_online)))
        for friend in friends_online:
            print("{0} {1}".format(friend["first_name"], friend["last_name"]))
    else:
        print("There aren't friends online.")



if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    try:
        friends_online = get_online_friends(login, password)
        output_friends_to_console(None)
    except vk.exceptions.VkAuthError:
        print("Should try again.")
