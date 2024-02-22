import random
from sources.data import database
import sources.art

print(sources.art.logo)
print("""Welcome to Higher - Lower Game!\n
    Rules:
    1. Computer gives you a question - which in two example has more followers
    2. You choose between first - 1 and second - 2\n""")


def random_account():
    account = random.choice(database)
    account_list = [account["name"], account["description"], account["country"], account["follower_count"]]
    account_output = f"{account_list[0]} - {account_list[1]} from {account_list[2]}"
    account_followers = account_list[3]
    return account_output, account_followers


def game():
    should_continue = True
    first_account = random_account()
    while should_continue:
        next_account = random_account()
        choose = int(
            input(f"1. {first_account}\n{sources.art.vs}\n2. {next_account}\n\nChoose: 1 or 2 has more followers: "))
        if choose == 1 or choose == 2:
            if choose == 1:
                if first_account[1] > next_account[1]:
                    print("Great!")
                else:
                    print("Wrong :(")
                    should_continue = False
            elif choose == 2:
                if first_account[1] < next_account[1]:
                    first_account = next_account
                    print("Great!")
                else:
                    print("Wrong :(")
                    should_continue = False
        else:
            print("Wrong number")


game()
