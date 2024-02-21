import random
from sources.data import database
import sources.art


# print(sources.art.logo)
# start_quit = input("""Welcome to Higher - Lower Game!\n
#     Rules:
#     1. Computer gives you a question - which in two example has more followers
#     2. You choose between first - 1 and second - 2\n
#     Press s to Start or q to Quit""")

def random_account():
    account = random.choice(database)
    account_list = [account["follower_count"], account["name"], account["description"], account["country"]]
    return account_list



