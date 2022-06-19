class Song:

    def __init__(self, name, artist, album, year):
        self.name = name
        self.artist = artist
        self.album = album
        self.year = year

    def __repr__(self):
        return f'\nName:   {self.name}' \
               f'\nArtist: {self.artist}' \
               f'\nAlbum:  {self.album}' \
               f'\nYear:   {self.year}'

