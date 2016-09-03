import requests
import bs4

locationsList = []

for number in range(1,17):
	url = "http://rovingpanda.com/4698/16-places-to-explore-in-your-20s/{}".format(number)
	r = requests.get(url).content
	soup = bs4.BeautifulSoup(r, "html.parser")
	#inspect elements, find where desired element is in html
	locations = soup.findAll('h1')
	locationsList.append(locations[1].getText())

print locationsList

