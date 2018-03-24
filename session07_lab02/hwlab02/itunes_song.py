from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"

# 1. Download web page
html_content = urlopen(url).read().decode("utf8")

# 2. Extract ROI (Region of Interest)
soup = BeautifulSoup(html_content,"html.parser")
section = soup.find("section","section chart-grid")

# 3. Extract Info
li_list = section.find_all("li")

songs = []

for li in li_list:
# 3.1 Create a dictionary
    song = {}
    a = li.h3.a
    song["name"] = a.string
    a = li.h4.a
    song["author"] = a.string
    songs.append(song)

pyexcel.save_as(records=songs, dest_file_name="itunes_song.xlsx")

options = {
"default_search" : "ytsearch",
"max_downloads" : 1,
"format" : "bestaudio/audio"
}

for song in songs:
    dl = YoutubeDL(options)
    dl.download([song["name"]])

# ytsearch
# dl.download(inner part)
