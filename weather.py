import requests,bs4,sys,warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")
weather_url = "https://weather.com/en-IN/weather/today/l/4f3d918cc51cf1ffee78e3d970943020f699d3480b25e6ca0baedd913b45746d"
res = requests.get(weather_url)
if res.raise_for_status() != None:
    print("Network error")
soup = bs4.BeautifulSoup(res.text)
nowcard = soup.findAll("span",{"class":""})
for elem in nowcard:
    if elem.parent.name == "div":
        attr = elem.parent.attrs
        try:
            chk = attr['class']
        except KeyError:
            pass
        if "today_nowcard-temp" in chk:
            temp = elem.text
            break
phrase = soup.find("div",{"class":"today_nowcard-phrase"}).text
print("Weather in Delhi")
print(temp + "C " + phrase)
table = soup.find("table")
table_body = table.find("tbody")
rows = table_body.find_all("tr")
for row in rows:
    head = row.find("th")
    cols = row.find_all("td")
    for elem in cols:
        print(head.text + " " + elem.text)

