from webbrowser import get
import requests
from bs4 import BeautifulSoup

def getAlbumDetails(albumName):
    
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

def getTrackHTML(track,suffix):
    URL = f"https://music.fandom.com/wiki/{track}{suffix}"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    trackHTML = soup.find_all("table",class_="vevent")
    return trackHTML

def getTrackDetails(track):

    trackHTML = getTrackHTML(track,"")    
    
    if len(trackHTML)==0:
        trackHTML = getTrackHTML(track,"_(song)")
        if len(trackHTML)==0:
            trackHTML = getTrackHTML(track,"_(Taylor_Swift_song)")
            if len(trackHTML)==0:
                return {"message":"Not enough data. Try other songs"}

    jsonData = dict()

    #Getting track name
    title = trackHTML[0].find("th",class_="summary")
    jsonData["title"] = title.text.strip()

    #Getting Image URL
    try:
        imgURL = trackHTML[0].find("a",{"class":"image"}).get("href")
        jsonData["image"] = imgURL
    except:
        pass

    #Getting Album Information
    infoKeys = trackHTML[0].find_all("th",attrs={"style":"width: 5.2em; text-align: left;"})
    infoValues = trackHTML[0].find_all("td",attrs={"style":"width: 14em;"})

    for i in range(len(infoKeys)):
        jsonData[infoKeys[i].text.strip()] = infoValues[i].text.strip()

    return jsonData