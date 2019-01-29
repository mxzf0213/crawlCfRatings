import requests
from bs4 import BeautifulSoup
import csv
import datetime

def getList():
    link = "https://codeforces.com/ratings/page/"
    headers = \
        {
            "Host": "codeforces.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"
        }

    rating_list = []
    rating_list.append(["Rank","Who","Number of participations","Score","Level"])
    for i in range(1,273):
        r = requests.get(link + str(i), headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        list = soup.find_all("table")[5].contents[3:]
        for eachone in list:
            now = []
            for x in range(1,8,2):
                now.append(eachone.contents[x].text.strip())
            now.append(' '.join(eachone.a.attrs["title"].split(' ')[:-1]))
            rating_list.append(now)
        print(i)

    return rating_list

if __name__ == "__main__":
    init_clock = datetime.datetime.now()
    personList = getList()
    end_clock = datetime.datetime.now()
    print(end_clock-init_clock)

    f = open("cfRating.csv","w",newline="")
    csv_writer = csv.writer(f)
    for each in personList:
        csv_writer.writerow(each)
    f.close()