def make_album(artist_name:str, album_title:str, song_number:int =None):
    if song_number is None:
        song_number = "unknow"
    return {"artist":artist_name, "album":album_title, "song numbers":song_number}

albums = [
        make_album("metallica","single",7),
        make_album("wuthering wave","sleeping jubilation"),
        make_album("vanguard sound","PGR OST")
        ]

for album in albums:
    print(f"artist: {album['artist']}, album: {album['album']}, song: {album['song numbers']}")


