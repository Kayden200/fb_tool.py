import os
import time
import requests
from bs4 import BeautifulSoup

def banner():
    os.system('clear')
    print("\033[95m")
    print("██████╗ ██╗   ██╗██╗     ███████╗")
    print("██╔══██╗██║   ██║██║     ██╔════╝")
    print("██████╔╝██║   ██║██║     █████╗  ")
    print("██╔═══╝ ██║   ██║██║     ██╔══╝  ")
    print("██║     ╚██████╔╝███████╗███████╗")
    print("╚═╝      ╚═════╝ ╚══════╝╚══════╝\033[0m")
    print("\033[94m      DEVELOPED BY RYLE - WORKING IN THE SHADOWS\033[0m")
    print("\033[95m========================================\033[0m")
    print(" YOUR FACEBOOK AUTOMATION TOOL")
    print("\033[95m========================================\033[0m")
    print("[01] FB React      -  Auto react to posts")
    print("[02] FB Spam Share -  Share posts multiple times")
    print("[03] FB Auto Create - Create Facebook accounts")
    print("[00] Exit")
    print("\033[95m========================================\033[0m")

def fb_login(email, password):
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36"
    }

    login_page = session.get("https://m.facebook.com/login", headers=headers)
    soup = BeautifulSoup(login_page.text, "html.parser")
    form = soup.find("form")
    
    if not form:
        print("\033[91m[!] Failed to load Facebook login page.\033[0m")
        return None

    action_url = form["action"]
    data = {tag["name"]: tag["value"] for tag in form.find_all("input") if tag.get("name")}
    data["email"] = email
    data["pass"] = password

    login_response = session.post(f"https://m.facebook.com{action_url}", data=data, headers=headers)

    if "c_user" in session.cookies:
        print("\033[92m[✔] Logged in successfully!\033[0m")
        return session
    else:
        print("\033[91m[!] Login failed! Check your credentials.\033[0m")
        return None

def fb_react():
    print("\n\033[92m[✔] Starting FB React...\033[0m")

    email = input("Enter your dummy Facebook email: ")
    password = input("Enter your dummy Facebook password: ")

    session = fb_login(email, password)
    if not session:
        return

    post_url = input("Enter the Facebook post URL: ")
    reaction_type = input("Choose reaction (like/love/haha/wow/sad/angry): ").lower()

    reactions = {
        "like": "1",
        "love": "2",
        "haha": "4",
        "wow": "3",
        "sad": "7",
        "angry": "8"
    }

    if reaction_type not in reactions:
        print("\033[91m[!] Invalid reaction type!\033[0m")
        return

    post_id = post_url.split("posts/")[-1].split("?")[0]
    react_url = f"https://m.facebook.com/reactions/picker/?ft_id={post_id}"
    
    react_page = session.get(react_url)
    soup = BeautifulSoup(react_page.text, "html.parser")
    react_buttons = soup.find_all("a", href=True)

    for button in react_buttons:
        if f"reaction_type={reactions[reaction_type]}" in button["href"]:
            session.get(f"https://m.facebook.com{button['href']}")
            print("\033[92m[✔] Reacted successfully!\033[0m")
            return

    print("\033[91m[!] Failed to react to the post.\033[0m")

def fb_spam_share():
    print("\n\033[92m[✔] FB Spam Share Feature Coming Soon!\033[0m")
    time.sleep(2)

def fb_auto_create():
    print("\n\033[92m[✔] FB Auto Create Feature Coming Soon!\033[0m")
    time.sleep(2)

while True:
    banner()
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
    time.sleep(2)
