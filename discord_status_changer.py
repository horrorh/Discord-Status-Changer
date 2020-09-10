# made by horrorhood
import random, os, requests, json, time

TOKEN = "put your token here"
DELAY = 1

STATUS = [
    "-> ecriminals <-",
    "-> kkk member <-",
    "-> お母さんゲイ <-",
    "-> anti-feminist <-",
    "-> nazi leader <-",
    "-> 客家です <-",
    "-> child predator <-",
    "-> rce in your mom puss <-",
    "-> 私は私の地下に子供がいます <-",
    "-> dropped a shell in your mom <-",
    "-> super hakka <-",
    "-> プロの中国のペンテスター <-"
]

def change_status(status):
    status_data = json.dumps(
            {
                "custom_status":
                {
                    "text": status
                }
            }
        )
    return requests.patch("https://discordapp.com/api/v6/users/@me/settings", headers={"Authorization": TOKEN, "Content-Type": "application/json"}, data=status_data)

def main():
    print("[+] Changing discord status.")
    while True:
        for stat in STATUS:
            change_status(stat)
            time.sleep(DELAY)



if __name__ == "__main__":
    main()
    