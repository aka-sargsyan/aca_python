from Playlist.Playlist import Playlist


class Player:

    def __init__(self, pl=None):
        if pl and not isinstance(pl, Playlist):
            raise TypeError('Second argument must be of type: Playlist')
        self.pl = pl
        self.__is_playing = False
        self.__current_song_index = 0

    def play(self, index=None):
        if not index:
            index = self.__current_song_index
        elif index >= len(self.pl.song):
            index = len(self.pl.song) - 1

        if index != self.__current_song_index:
            self.__current_song_index = index
        elif self.__is_playing:
            print('player is already on')
            return None

        self.__is_playing = True
        print(f'now playing <<<{self.pl.song[index].name}>>> song')

    def stop(self):
        if self.__is_playing:
            self.__is_playing = False
            print('Player is off')
        else:
            print('player is already stop')

    def next_song(self):
        if self.__is_playing:
            self.play(self.__current_song_index + 1)
        else:
            print('player can not play song, you must play it')
