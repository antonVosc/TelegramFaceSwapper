from bs4 import BeautifulSoup
from urllib.request import urlopen

requests_url = None

def get_url():
    page = urlopen("https://www.faceswapper.app/")
    soup = BeautifulSoup(page.read())
    results = soup.find_all("script")
    tag = results[-2]
    text = tag.text.split(";")

    for i in text:
        if "status" in i:
             text = i.split("'")
             request_url = text[-6]


    request_url = "https://"+request_url+".ngrok-free.app/swapper/api.php"

    return request_url