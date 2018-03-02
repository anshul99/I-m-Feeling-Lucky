import sys,pyperclip,bs4,requests,warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")
if len(sys.argv) > 1:
    ip = "".join(sys.argv[1:])
else:
    ip = pyperclip.paste()
print("ip:\t\t",ip)
print("\nWait for a few moments...\n")
url = "https://www.whois.com/whois/" + ip
res = requests.get(url)
if res.raise_for_status() != None:
    print("Network Error")
soup = bs4.BeautifulSoup(res.text)
error = soup.find("div", {"class":"whois_errorbox"})
if error:
    error = error.getText()
    print(error)
else:
    info = soup.find("div", {"class":"df-block"})
    info = info.getText()
    i = info.index("person")
    info = info[i:]
    j = info.index("%")
    info = info[:j] 
    print(info)
input("Press enter to quit")
