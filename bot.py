import os
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


def get_json(url):
    request = requests.get(url)
    if request.status_code == 200:
        return json.loads(request.content)
    return None


def mark_read(offset):
    answer = get_json(URL + "/getUpdates?offset={}".format(offset))


def get_updates():
    answer = get_json(URL + "/getUpdates")
    if answer is None and answer["ok"]:
        return

    print(answer)

    for result in answer["result"]:
        yield result


def list_files(path):
    return os.listdir(path)


def parse_payload(command):
    if command == "ls":
        files = list_files("./")
        print(files)


if __name__ == "__main__":
    update_id = 0

    for update in get_updates():
        update_id = update["update_id"] + 1
        print(update)
        parse_payload(update["message"]["text"])
    #mark_read(update_id)
