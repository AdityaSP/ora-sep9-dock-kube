import requests
import json
import os
from threading import Thread

moviename = input("Enter a movie name: ")
if os.path.exists(moviename):
    res= input("Already exists.Do you want to overwrite?: ")
    if res.strip().upper() not in ['Y', 'YES','1']:
        print("Exiting..")
        exit(-1)
else:        
    os.mkdir(moviename)

r = requests.get(r'http://www.omdbapi.com/?s='+ moviename +'&apikey=b4e17ea0')

def download(posterurl, loc):
    poster = requests.get(posterurl)
    if poster.ok:
        fh = open( loc ,'wb')
        fh.write(poster.content)
        fh.close()
    print("Download done for ", posterurl)    

if r.ok:
    data = json.loads(r.text)
    for movie in data['Search']:
        print("Downloading poster for ", movie['Title'])
        posterurl = movie['Poster']
        if posterurl != 'N/A':
#            download(posterurl, moviename + os.path.sep +movie['imdbID'] + ".jpg")
             t = Thread(target=download, args=(posterurl, moviename + os.path.sep +movie['imdbID'] + ".jpg"))   
             t.start()
             