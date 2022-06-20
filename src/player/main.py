from Player.Player import Player
from Song.Song import Song
from Playlist.Playlist import Playlist

if __name__ == '__main__':

    pl = Playlist()
    pl.load_songs('./data/albums.txt')
    # print(pl)
    p = Player(pl)
    p.play(1)
    p.play(15)
    # p.stop()
    # p.play(2)
    # p.stop()
    # p.play()
    # p.next_song()
    # p.play(-5)
    # p.previous_song()
    # p.show_current_song()
    # print(p)
