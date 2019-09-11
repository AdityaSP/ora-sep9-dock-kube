import requests
import json
moviename = input("Enter a movie name: ")

r = requests.get(r'http://www.omdbapi.com/?s='+ moviename +'&apikey=b4e17ea0')

if r.ok:
    data = json.loads(r.text)
    for movie in data['Search']:
        print("Downloading poster for ", movie['Title'])
        posterurl = movie['Poster']
        if posterurl != 'N/A':
            poster = requests.get(posterurl)
            if poster.ok:
                fh = open( movie['imdbID'] + ".jpg" ,'wb')
                fh.write(poster.content)
                fh.close()