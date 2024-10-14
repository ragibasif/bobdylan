from bs4 import BeautifulSoup
import requests

BASE_URL = "https://en.wikipedia.org"
# wikipedia rejects the request unless the user agent is added
HEADERS = {"User-Agent": "Mozilla/5.0"}


def get_Bob_Dylan_soup():
    response = requests.get(
        BASE_URL + "/wiki/List_of_awards_and_nominations_received_by_Bob_Dylan",
        headers=HEADERS,
    )
    return BeautifulSoup(response.content, "lxml")


soup = get_Bob_Dylan_soup()
soup_find = soup.find("table", {"class": "wikitable"})
soup_select = soup.select("table.wikitable")
print(soup_select)
