import requests
from bs4 import BeautifulSoup

def getAlbumDetails(albumName):
    #testing

    if albumName=="Taylor Swift":
        suffix = "(album)"
    else:
        suffix = "(Taylor_Swift_album)"

    URL = f"https://music.fandom.com/wiki/{albumName}_{suffix}"
    page = requests.get(URL)

    jsonData = dict()

    soup = BeautifulSoup(page.content, "html.parser")

    albumHTML = soup.find_all("aside",class_="portable-infobox pi-background pi-border-color pi-theme-wikia pi-layout-default")

    #Getting album name
    title = albumHTML[0].find("h2",class_="pi-item pi-item-spacing pi-title pi-secondary-background")
    jsonData["title"] = title.text

    #Getting Album Image url
    imgURL = albumHTML[0].find("a",{"class":"image image-thumbnail"}).get("href")
    jsonData["image"] = imgURL


    #Getting Album Information
    infoKeys = albumHTML[0].find_all("h3",class_="pi-data-label pi-secondary-font")
    infoValues = albumHTML[0].find_all("div",class_="pi-data-value pi-font")
    for i in range(len(infoKeys)):
        jsonData[infoKeys[i].text] = infoValues[i].text


    #Getting tracks
    tracksHTML = soup.find_all("table",class_="tracklist")
    allTracks = [track.text.strip().replace('"','') for track in tracksHTML[0].find_all("td",attrs={"style":"text-align: left; vertical-align: top;"})]
    jsonData["Tracks"] = allTracks

    return jsonData


def getTrackDetails(trackName):
    pass

albumName = input("Enter Album name: ")
print(getAlbumDetails(albumName))


# {
#     'title': 'Red', 
#     'image': 'https://static.wikia.nocookie.net/music/images/f/f2/Red_TS.jpg/revision/latest?cb=20210118221401', 
#     'Artist': 'Taylor Swift', 
#     'Released': 'October 22, 2012', 
#     'Recorded': '2011-2012', 
#     'Genre': 'Pop, country, rock', 
#     'Length': '65:11', 
#     'Language': 'English', 
#     'Label': 'Big Machine', 
#     'Producer': 'Taylor Swift, Nathan Chapman,', 
#     'Tracks': ['State Of Grace', 'Red', 'Treacherous', 'I Knew You Were Trouble', 'All Too Well', '22', 'I Almost Do', 'We Are Never Ever Getting Back Together', 'Stay Stay Stay', 'The Last Time', 'Holy Ground', 'Sad Beautiful Tragic', 'The Lucky One', 'Everything Has Changed', 'Starlight', 'Begin Again']
# }

