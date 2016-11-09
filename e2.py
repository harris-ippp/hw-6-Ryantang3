from bs4 import BeautifulSoup

import requests

for line in open("ELECTION_ID"):
    year,id = (int(x) for x in line.split())
    url = "http://historical.elections.virginia.gov/elections/download/" + str(id) + "/precincts_include:0/"
    resp  = requests.get(url)
    data = resp.text
    file_name = str(year) +".csv"
    with open(file_name, "w") as out:
        out.write(data)
