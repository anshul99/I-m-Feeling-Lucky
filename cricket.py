import requests,bs4,sys,warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")
url = "http://www.espncricinfo.com/scores"
res = requests.get(url)
if res.raise_for_status() != None:
    print("Network error")
soup = bs4.BeautifulSoup(res.text)
all_games = soup.find("div",{"class":"scoreCollection__content cricket"})
for game in all_games:
    curr = game.find("ul")
    teams = curr.findAll("span",{"class":"cscore_name cscore_name--long"})
    scores = curr.findAll("div",{"class":"cscore_score"})
    info = game.find("div",{"class":"cscore_date-time"})
    overview = game.find("div",{"class":"cscore_info-overview"}).text
    date = info.find("span",{"class":"cscore_date"})
    time = info.find("span",{"class":"cscore_time"})
    if date != None and time != None:
        match_state = time.text + " " + game.find("span",{"class":"cscore_notes_game"}).text
    else:
        match_state = game.find("span",{"class":"cscore_notes_game"}).text
    team1 = teams[0].text
    score1 = scores[0].text
    team2 = teams[1].text
    score2 = scores[1].text
    print(overview)
    print(team1,score1)
    print(team2,score2)
    print(match_state)
    print()
