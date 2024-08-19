class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def total_duration(self):
        duration = 0
        for song in self.songs:
            duration += song.duration
        return duration

class Spotify:
    def __init__(self):
        self.playlists = []

    def create_playlist(self, name):
        playlist = Playlist(name)
        self.playlists.append(playlist)

    def add_song_to_playlist(self, playlist_name, song):
        for playlist in self.playlists:
            if playlist.name == playlist_name:
                playlist.add_song(song)
                break

    def remove_song_from_playlist(self, playlist_name, song):
        for playlist in self.playlists:
            if playlist.name == playlist_name:
                playlist.remove_song(song)
                break

    def display_playlists(self):
        print("Playlists:")
        for playlist in self.playlists:
            print("- " + playlist.name)

    def display_songs(self, playlist_name):
        for playlist in self.playlists:
            if playlist.name == playlist_name:
                print("Songs in playlist '" + playlist_name + "':")
                if len(playlist.songs) == 0:
                    print("No songs in this playlist.")
                else:
                    for song in playlist.songs:
                        print("- " + song.title + " by " + song.artist)
                break

song1 = Song("Song 1", "Artist 1", 180)
song2 = Song("Song 2", "Artist 2", 240)
song3 = Song("Song 3", "Artist 3", 200)

spotify = Spotify()
playlist1 = Playlist("Playlist 1")
playlist1.add_song(song1)
playlist1.add_song(song2)
spotify.playlists.append(playlist1)

while True:
    print("Menu:")
    print("1. Create a new playlist")
    print("2. Add a song to a playlist")
    print("3. Remove a song from a playlist")
    print("4. Display playlists")
    print("5. Display songs in a playlist")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter the name of the new playlist: ")
        spotify.create_playlist(name)
    elif choice == "2":
        spotify.display_playlists()
        playlist_name = input("Enter the name of the playlist: ")
        title = input("Enter the title of the song: ")
        artist = input("Enter the artist of the song: ")
        duration = int(input("Enter the duration of the song in seconds: "))
        song = Song(title, artist, duration)
        spotify.add_song_to_playlist(playlist_name, song)
    elif choice == "3":
        spotify.display_playlists()
        playlist_name = input("Enter the name of the playlist: ")
        spotify.display_songs(playlist_name)
        title = input("Enter the title of the song to remove: ")
        for playlist in spotify.playlists:
            if playlist.name == playlist_name:
                for song in playlist.songs:
                    if song.title == title:
                        spotify.remove_song_from_playlist(playlist_name, song)
                        break
                break
    elif choice == "4":
        spotify.display_playlists()
    elif choice == "5":
        spotify.display_playlists()
        playlist_name = input("Enter the name of the playlist: ")
        spotify.display_songs(playlist_name)
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")