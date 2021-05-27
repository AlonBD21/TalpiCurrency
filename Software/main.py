from Logic.User import *
from Software.Server import *
from Software.Client import *
from Support.CryptoJson import string_to_bytes
from Support.CryptoJson import bytes_to_string

def new_user():
    user = User.generate ()
    return user


def mine(user):
    server = Server(user)
    server.start_server()


def trade(user):
    client = Client (user)
    while True:
        result = input ("do you want to Send transaction or get Balance? ST/GB")
        if result == "ST":
            send_to = input ("who do you want to send it to?")
            send_to = string_to_bytes(send_to)
            amount = input ("how much?")
            client.broadcast_transaction (send_to, amount)
        elif result == "GB":
            balance = client.ask_balance ()
            print ("your balance is", balance, "Coin-ף")


def retrive_user():
    global result, user
    result = input ("do you already have a user? Y/N")
    if result == "N":
        user = new_user ()
        print ("This is your secret key, write it somewhere safe:", bytes_to_string(user.get_sk_bytes ()))
    elif result == "Y":
        sk = input ("enter secret key:")
        user = User.from_sk_bytes (string_to_bytes(sk))
    elif result == "q":
        return None
    return user


def begin_with_new_user():
    user = retrive_user ()
    if not user:
        print ("BYE")
        exit ()
    result = input ("do you want to mine of trade? M/T")
    while True:
        if result == "M":
            mine (user)
        elif result == "T":
            trade (user)
        elif result == "q":
            result2 = input ("Hmmm, do you want to enter from other user? Y/N")
            if result2 == "N":
                print ("BYE")
                exit ()
            elif result2 == "Y":
                begin_with_new_user ()


if __name__ == "__main__":
    print ("Wellcome to ף-Coin!")
    print ("if you want to exit press q")
    begin_with_new_user ()
