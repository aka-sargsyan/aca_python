from Song.Song import Song


class Playlist:

    def __init__(self):
        self.song = []

    def load_songs(self, path):
        """
        :param path is address file albums.txt:
        n is name
        a is artist
        al is albums
        y is year
        :return:
        """
        with open('./' + path, 'r') as file:
            for list_song in file:
                a, al, y, n = tuple(list_song.strip().split('\t'))
                self.song.append(Song(n, a, al, y))

    def show_songs(self):
        for song in self.song:
            print(f'{song.name}......{song.artist}')

    def __str__(self):
        return f'our songs are {len(self.song)}'
