class Song:
    count = 0
    genres = []
    artists = []
    genres_count = {}
    artists_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class-level attributes
        Song.add_song_to_counts()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)

    @classmethod
    def add_song_to_counts(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre not in cls.genres_count:
            cls.genres_count[genre] = 0
        cls.genres_count[genre] += 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist not in cls.artists_count:
            cls.artists_count[artist] = 0
        cls.artists_count[artist] += 1
