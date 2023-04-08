import requests
import json
import time
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("github.com/nismo1337 | nismo#1337 | t.me/nismo1337")

url = "https://api.mojang.com/users/profiles/minecraft/%s"

webhook_url = "haii :33"

with open("usernames.txt", "r") as file:
    usernames = file.read().splitlines()

checked_usernames = set()

while True:
    for username in usernames:
        if username in checked_usernames:
            continue

        response = requests.get(url % username)

        if response.status_code != 200:
            with open("available_usernames.txt", "a") as output_file:
                output_file.write(username + "\n")

            data = {
                "embeds": [
                    {
                        "title": "Username available: " + username,
                        "color": 65280
                    }
                ]
            }

            response = requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})

            if response.status_code == 204:
                print("Webhook sent successfully for " + username)
            else:
                print("Webhook sending failed with status code " + str(response.status_code) + " for " + username)

        checked_usernames.add(username)

    time.sleep(10)
