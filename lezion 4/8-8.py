def make_album(artist_name:str, album_title:str, song_number:int =None) ->dict:
    if song_number is None:
        song_number = "unknow"
    return {"artist":artist_name, "album":album_title, "song numbers":song_number}

while True:
    aritist_name:str=input("inserici un artista:")
    album_title:str=input("inserici un album:")
    break
  
    

print(make_album(aritist_name,album_title))
