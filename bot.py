import requests
import json 
from authorization import TOKEN

URL = "https://api.telegram.org/bot{}".format(TOKEN)


def get_status():
    answer = requests.get(URL + "/getme")
    if answer.status_code == 200:
        print("Connection works")
    else:
        print("Connection does not work")


if __name__ == "__main__":
    get_status()

