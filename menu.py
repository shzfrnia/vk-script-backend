#!/usr/local/bin/python3

import serviceVk
import accountWithoutLogin
import sys

anon = accountWithoutLogin.AccountWithoutLogin()
service = serviceVk.ServiceVk()
auth = False
account = None
print(r""" _____________________________________
/ Welcom to my first program!          \
\ (c)Mikhail Ulyakov (vk.com/shzfrnia) /
 -------------------------------------
 \
  \
   \ >()_
      (__)__ _""")

while True:
    print("Menu")
    print(f"""1) Set user \n2) Show banned and deleted account in friends \n3) Exit \nCurrently account: {account}""")
    answer = input()

    
    if answer == "3":
        break

    elif answer == "1":
        anon_id = input("Input vk id: ")
        try:
            service.check_id_on_exists(anon_id)
        except:
            print("****************")
            print(f"""Syrry, but account {"vk.com/" + anon_id} is not exists.\nPlease, try again""")
            print("****************")
            continue
        anon.set_account(anon_id)
        account = anon.get_info_about_account()
        auth = True
        account = (f'{account["first_name"]} {account["last_name"]} ({account["link"]}).\n')

    elif (answer == "2"):
        if auth == False:
            print("\n***Pleasy, set user***\n")
            continue
        ban_and_del_acc = anon.get_banned_and_deleted_friends()
        ban_acc = ban_and_del_acc["banned"]
        del_acc = ban_and_del_acc["deleted"]
        print("****************")
        print(f'All friends: ({anon.get_count_friends()}).')
        print("Your banned friends: ")
        for banned_account in ban_acc:
            print(f'{banned_account["first_name"]} {banned_account["last_name"]} ({banned_account["link"]})')
        print(f'    Count: {"You havent banned accounts in friends" if (anon.get_count_banned() == 0) else {anon.get_count_banned()}}')
        print("Your deleted friends: ")
        for deleted_account in del_acc:
            print(f'{deleted_account["first_name"]} {deleted_account["last_name"]} ({deleted_account["link"]})')
        print(f'    Count: {"You havent deleted accounts in friends" if (anon.get_count_deleted() == 0) else {anon.get_count_deleted()}}')
        print("****************")