from bs4 import BeautifulSoup
import requests

ELECTION_ID = {}
url = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2015/office_id:1/stage:General"
r  = requests.get(url)
data = r.text

soup = BeautifulSoup(data, "html.parser")
rows = soup.find_all("tr")

for row in rows:
    id = str(row.get("id"))
    begin = id.find("election-id-")
    if (begin != -1):
        election_id  = id[12:]
        cell = row.find("td")
        year = cell.string
        ELECTION_ID[year] = election_id

for k,v in sorted(ELECTION_ID.items(), reverse=True):
    print (k,v)
