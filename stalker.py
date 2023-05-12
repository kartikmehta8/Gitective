import requests
from bs4 import BeautifulSoup
import time
from sms import send_sms
from clone import clone_repository

USERNAME = "TARGET_USERNAME"
prevCount = 0

while True:
    url = f"https://github.com/{USERNAME}?tab=repositories"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    repositories = soup.find_all("a", {"itemprop": "name codeRepository"})

    currCount = len(repositories)

    if currCount > prevCount and prevCount != 0:
        clone_repository(
            f"https://github.com{repositories[0]['href']}.git",
            "YOUR_USERNAME",
            "YOUR_PASSWORD",
            f"./{repositories[0].text.strip()}",
        )
        send_sms(
            repositories[0].text.strip(),
            f"https://github.com{repositories[0]['href']}",
            USERNAME,
        )

    else:
        print("No new repository added within the last 24 hours.")
    prevCount = currCount

    time.sleep(60*60*24)
