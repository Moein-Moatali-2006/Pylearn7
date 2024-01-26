from media import Media


class Actor(Media):
    def __init__(self, name, director, IMDB_score, url, duration, casts):
        super().__init__(name, director, IMDB_score, url, duration, casts)

    
    def show_actor(self):
        ...