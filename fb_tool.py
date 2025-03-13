import os
import time
import requests
from bs4 import BeautifulSoup

# ✅ Machine Liker URLs
MACHINE_LIKER_LOGIN = "https://machine-liker.com/login"
MACHINE_LIKER_BOOST = "https://machine-liker.com/boost"

# ✅ Function to log in to Machine Liker
def machine_liker_login(email, password):
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.153 Mobile Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://machine-liker.com/",
    }

    login_page = session.get(MACHINE_LIKER_LOGIN, headers=headers)

    if login_page.status_code != 200:
        print("\033[91m[!] Failed to load Machine Liker login page.\033[0m")
        return None

    soup = BeautifulSoup(login_page.text, "html.parser")
    form = soup.find("form")

    if not form:
        print("\033[91m[!] Could not find login form on Machine Liker.\033[0m")
        return None

    data = {tag["name"]: tag.get("value", "") for tag in form.find_all("input") if tag.get("name")}
    data["email"] = email
    data["password"] = password

    login_response = session.post(MACHINE_LIKER_LOGIN, data=data, headers=headers)

    if "session" in session.cookies:
        print("\033[92m[✔] Logged in to Machine Liker successfully!\033[0m")
        return session
    else:
        print("\033[91m[!] Machine Liker login failed!\033[0m")
        return None

# ✅ Function for FB React (Using Machine Liker)
def fb_react():
    print("\n\033[92m[✔] Starting FB React...\033[0m")

    email = input("Enter your dummy Facebook email: ")
    password = input("Enter your dummy Facebook password: ")

    session = machine_liker_login(email, password)
    if not session:
        return

    print("\n\033[96mChoose a reaction:\033[0m")
    reactions = {
        "1": "Like",
        "2": "Love",
        "3": "Haha",
        "4": "Wow",
        "5": "Sad",
        "6": "Angry"
    }

    for key, value in reactions.items():
        print(f"[{key}] {value}")

    reaction_choice = input("\033[96mEnter your choice (1-6): \033[0m")
    
    if reaction_choice not in reactions:
        print("\033[91m[!] Invalid reaction type!\033[0m")
        return

    post_url = input("\033[96mEnter the Facebook post URL: \033[0m")

    boost_data = {
        "post_url": post_url,
        "reaction": reactions[reaction_choice]
    }

    boost_response = session.post(MACHINE_LIKER_BOOST, data=boost_data)

    if boost_response.status_code == 200:
        print("\033[92m[✔] Reaction boosted successfully!\033[0m")
    else:
        print("\033[91m[!] Failed to boost reaction.\033[0m")

# ✅ Function for FB Spam Share
def fb_spam_share():
    print("\n\033[92m[✔] FB Spam Share Feature Coming Soon!\033[0m")
    time.sleep(2)

# ✅ Function for FB Auto Create (Using TempMail)
def fb_auto_create():
    print("\n\033[92m[✔] FB Auto Create Feature Coming Soon!\033[0m")
    time.sleep(2)

# ✅ Main Menu
while True:
    os.system('clear')
    print("\n\033[95m==== FB AUTOMATION TOOL ====\033[0m")
    print("[1] FB React - Auto boost reactions")
    print("[2] FB Spam Share - Auto share posts")
    print("[3] FB Auto Create - Create new FB accounts")
    print("[0] Exit")

    choice = input("\033[96mEnter your choice: \033[0m")

    if choice == "1":
        fb_react()
    elif choice == "2":
        fb_spam_share()
    elif choice == "3":
        fb_auto_create()
    elif choice == "0":
        print("\n\033[91mExiting... Goodbye!\033[0m")
        break
    else:
        print("\n\033[91mInvalid choice! Try again.\033[0m")
