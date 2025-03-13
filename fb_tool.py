import os
import time
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

def fb_login(driver, email, password):
    driver.get("https://www.facebook.com/login")
    time.sleep(3)

    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "pass").send_keys(password, Keys.RETURN)
    time.sleep(5)

    if "checkpoint" in driver.current_url:
        print("\033[91m[!] Facebook Checkpoint Detected. Solve it manually.\033[0m")
        return False
    print("\033[92m[✔] Logged in successfully!\033[0m")
    return True

def fb_react():
    print("\n\033[92m[✔] Starting FB React...\033[0m")
    
    # User enters dummy Facebook account
    email = input("Enter your dummy Facebook email: ")
    password = input("Enter your dummy Facebook password: ")

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = uc.Chrome(options=options)

    if not fb_login(driver, email, password):
        driver.quit()
        return

    # User chooses reaction type
    post_url = input("Enter the Facebook post URL: ")
    reaction_type = input("Choose reaction (like/love/haha/wow/sad/angry): ").lower()

    reactions = {
        "like": "Like",
        "love": "Love",
        "haha": "Haha",
        "wow": "Wow",
        "sad": "Sad",
        "angry": "Angry"
    }

    if reaction_type not in reactions:
        print("\033[91m[!] Invalid reaction type!\033[0m")
        driver.quit()
        return

    driver.get(post_url)
    time.sleep(3)

    try:
        react_button = driver.find_element(By.XPATH, f"//div[@aria-label='{reactions[reaction_type]}']")
        react_button.click()
        print("\033[92m[✔] Reacted successfully!\033[0m")
    except:
        print("\033[91m[!] Could not find the react button.\033[0m")

    driver.quit()

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
