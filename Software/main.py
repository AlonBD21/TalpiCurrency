from Logic.User import User
from Software.Server import Server
from Software.Client import Client
from Support.CryptoJson import string_to_bytes
from Support.CryptoJson import bytes_to_string
import colorama
from colorama import Fore, Back, Style

colorama.init (autoreset=True)
# BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET
# DIM NORMAL BRIGHT RESET ALL

MONEY = f"{Back.WHITE}{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}ף-Coin!"
YES_NO = F"{Fore.GREEN}Y{Fore.WHITE}{Style.BRIGHT}/{Fore.RED}N"

def new_user():
    user = User.generate ()
    return user


def mine(user):
    server = Server (user)
    server.start_server ()


def trade(user):
    client = Client (user)
    while True:
        result = input (
            f"{Style.BRIGHT}do you want to Get Balance or Send Transaction? {Fore.GREEN}GB{Style.BRIGHT}/{Fore.RED}ST ")
        if result == "ST":
            send_to = input (f"{Fore.BLUE}who do you want to send it to? ")
            if send_to in "qQ":
                try_again ()
            send_to = string_to_bytes (send_to)
            amount = input (f"{Fore.BLUE}how much {MONEY}{Style.RESET_ALL}{Fore.BLUE} ? ")
            if amount in "qQ":
                try_again ()
            client.broadcast_transaction (send_to, amount)
        elif result == "GB":
            balance = client.ask_balance ()
            print (f"{Fore.YELLOW}$$$$$$$$$$$$$$$$$$$$$$$$$$")
            print (f"{Fore.YELLOW}your balance is {balance} {MONEY}")
            print (f"{Fore.YELLOW}$$$$$$$$$$$$$$$$$$$$$$$$$$")
        elif result in "qQ":
            try_again ()


def retrive_user():
    global result, user
    result = input (f"do you already have a user? {YES_NO} ")
    if result == "N":
        user = new_user ()
        print (
            f"{Fore.LIGHTRED_EX}This is your secret key, write it somewhere safe:\n{bytes_to_string (user.get_sk_bytes ())}")
        print(f"{Fore.LIGHTBLUE_EX}This is your public key:\n{bytes_to_string(user.get_vk_bytes())}")
    elif result == "Y":
        sk = input (f"{Fore.BLUE}enter secret key: ")
        if sk in "Qq":
            my_exit ()
        user = User.from_sk_bytes (string_to_bytes (sk))
    elif result in "Qq":
        my_exit ()
    return user


def begin_with_new_user():
    user = retrive_user ()
    if not user:
        my_exit ()
    result = input (f"do you want to mine of trade? {Fore.GREEN}M{Style.BRIGHT}/{Fore.RED}T ")
    while True:
        if result == "M":
            mine (user)
        elif result == "T":
            trade (user)
        elif result in "Qq":
            try_again ()


def try_again():
    result2 = input (f"Hmmm, do you want to enter from other user? {YES_NO} ")
    if result2 == "N":
        my_exit ()
    elif result2 == "Y":
        begin_with_new_user ()


def my_exit():
    print (f"{Fore.LIGHTCYAN_EX}------------------------------------------")
    print (f"{Style.BRIGHT}{Fore.CYAN}Goodbye! We hope you enjoyed using {MONEY}")
    print (f"{Fore.LIGHTCYAN_EX}------------------------------------------")
    exit ()


if __name__ == "__main__":
    print (f"{Fore.LIGHTCYAN_EX}-------------------")
    print (f"{Style.BRIGHT}{Fore.CYAN}Wellcome to {MONEY}")
    print (f"{Fore.LIGHTCYAN_EX}-------------------")
    print (f"{Style.BRIGHT}{Fore.LIGHTBLUE_EX}at any time, if you want to exit press q")
    begin_with_new_user ()
