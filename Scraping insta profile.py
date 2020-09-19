from bs4 import BeautifulSoup
import requests

URL = "https://www.instagram.com/{}/"
def parse_data(s):
  data = {}
  s = s.split("_")[0]
  s = s.split(" ")
  data['Followers'] = s[0]
  data['Following'] = s[2]
  data['Post'] = s[4]
  return data

def scrape_data(username):
  r = requests.get(URL.format(username))
  s = BeautifulSoup(r.text, "html.parser")
  meta = s.find("meta",property = "og:description")
  return parse_data(meta.attrs['content'])

if __name__ == "__main__":
  username = "white_devil_280"
  data = scrape_data(username)
  print(data)
