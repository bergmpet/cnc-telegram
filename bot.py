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


def get_updates():
    answer = get_json(URL + "/getUpdates")
    if answer is None and answer["ok"]:
        return

    # testing
    print(answer)
    data = answer["result"][0]
    print(data)
    print(data["message"])


if __name__ == "__main__":
    get_updates()
