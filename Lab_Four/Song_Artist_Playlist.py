class Song:
    def __init__(self,name,title,time):
        self.artist_name = name
        self.song_title = title
        self.time_duration = time

    def print_song_info(self):
        print(f"This song is by {self.artist_name} and is called {self.song_title}, it is {self.time_duration} seconds long") 

class Artist:
    def __init__(self,name):
        self.artist_name = name
        self.songs = list()

    def add_song(self,song):
        self.songs.append(song)

    def print_song_list(self):
        print('Song list for ',self.artist_name)
        for song in self.songs:
            song.print_song_info()
    
class Playlist:
    def __init__(self,playlist_name):
        self.playlist_name = playlist_name
        self.songs = list()

    def add_song(self,song):
        self.songs.append(song)

    def print_song_list(self):
        print('Song list for ',self.playlist_name, 'Playlist')
        for song in self.songs:
            song.print_song_info()

def main():
    #defined three artists
    artist_one = Artist("Wand")
    artist_two = Artist("The Murlocs")
    artist_three = Artist("Sparks")

    #defined three songs that used artists names
    song_one=Song(artist_one.artist_name,"Fire On The Mountain",555)
    song_two=Song(artist_two.artist_name,"What If?", 345)
    song_three=Song(artist_three.artist_name,"Slowboat",630)

    #defined playlist and added all songs to it
    playlist_one = Playlist(playlist_name='Certified Bangerz and Mash')
    playlist_one.add_song(song_one)
    playlist_one.add_song(song_two)
    playlist_one.add_song(song_three)

    #added songs to each artist
    artist_one.add_song(song_one)
    artist_two.add_song(song_two)
    artist_three.add_song(song_three)

    #printed artists lists and playlist
    artist_one.print_song_list()
    print('---')
    artist_two.print_song_list()
    print('---')
    artist_three.print_song_list()
    print ('#######')
    playlist_one.print_song_list()

main()