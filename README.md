# Taylor Swift API🎵

## Description:
Taylor Swift API is a RESTful API made using Python and Flask. Using this API, one can get the information of Taylor Swift's albums and tracks. The API scraps information from this [site](https://music.fandom.com/wiki/Taylor_Swift) using BeautifulSoup library and returns the information in JSON format.

## How to use:
### Album Details:
**Syntax:** 

    https://taylorswift-api.herokuapp.com/albums/{album name}
    
 **Example:**
 
     https://taylorswift-api.herokuapp.com/albums/red
    
 **Output:**
 
 <img width="721" alt="albums" src="https://user-images.githubusercontent.com/80971180/180500344-41b3aceb-e45e-4b91-91d2-ff2402bdd0e4.png">
 
 ### Track Details:
**Syntax:** 

    https://taylorswift-api.herokuapp.com/tracks/{track name}
    
 **Example:**
 
     https://taylorswift-api.herokuapp.com/tracks/Wildest Dreams
    
 **Output:** 

<img width="682" alt="tracks" src="https://user-images.githubusercontent.com/80971180/180500757-c442dbda-cfdb-4742-91ac-72539aa4151b.png">


**Note:** Album and track names are case and space sensitive. So, check properly while entering the names in the API.
