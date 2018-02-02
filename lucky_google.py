# Opens top 7 Google search results
import requests,webbrowser,bs4
x = input()
print("Wait for a few moments...")
res = requests.get("https://www.google.co.in/search?q=" + " ".join(x))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
linkElems = soup.select(".r a")
numTabs = min(7,len(linkElems))
webbrowser.open("https://www.google.co.in/search?q=" + x)
for i in range(numTabs):
    webbrowser.open("https://www.google.co.in" + linkElems[i].get("href"))
