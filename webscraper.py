from bs4 import BeautifulSoup
import requests


url = "https://chartmasters.org/most-streamed-artists-ever-on-spotify/"
r = requests.get(url)


soup = BeautifulSoup(r.text, 'html.parser')


artist_table = soup.find('table',class_ =  'responsive display nowrap data-t data-t wpDataTable wpDataTableID-1')


for art in artist_table.find_all('tbody'):
    rows = art.find_all('tr')
    
    for row in rows:
        artist = row.find('td' , class_ = "column-artist")
        return(artist)
        

        
# Code snippet for Spotify webscraper project

        


