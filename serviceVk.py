#!/usr/local/bin/python3

import requests
import os
import json
import user

class ServiceVk():
    __ACCESS_TOKEN = os.environ["VK_ACCESS_TOKEN"]
    __VK_API = "https://api.vk.com/method/"
    __ACCOUNT_LINK = "https://vk.com/"
    __API_VERSION = "5.80"
    __LANGUAGE = "ru"
    __vk_user = user.User()
    
    def request_info_of_account(self, vk_account_id):
        account_info = self.__request_json("users.get", params={"user_ids": vk_account_id})["response"][0]
        self.__vk_user.set_user(account_info)
        self.__vk_user["link"] = self.__ACCOUNT_LINK + "id" + self.__vk_user["id"]
        return self.__vk_user

    def check_id_on_exists(self, vk_account_id):
        request_info_of_user = self.__request_json("users.get", params={"user_ids": vk_account_id})
        if "error" in request_info_of_user:
            raise IOError(request_info_of_user["error"]["error_msg"])
        elif len(request_info_of_user["response"]) == 0:
            raise IOError("Sorry but account isn't exists")
        elif "deactivated" in request_info_of_user["response"][0]:
            raise IOError("Try again this account is: " + request_info_of_user["response"][0]["deactivated"])
        return True

    def __request_json(self, method, params):
        vk_method =         self.__VK_API + str(method)
        vk_access_token =   "?access_token=" + self.__ACCESS_TOKEN
        vk_api_v =          "&v=" + self.__API_VERSION
        vk_lang =           "&lang=" + self.__LANGUAGE
        req = requests.get(vk_method + vk_access_token + vk_api_v + vk_lang, params)
        json_data = req.json()
        return json_data
    
    def requests_public_friend_list(self, vk_account_id, fields = "online"):
        parametrs = {"order":   "name",
                     "fields":  fields,
                     "user_id": vk_account_id}
        req = self.__request_json("friends.get", parametrs)
        friends_list = req["response"]["items"]
        for friend in friends_list:
            friend["link"] = ("https://vk.com/id" + str(friend["id"]))
        return friends_list