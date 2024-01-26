from media import Media


class Series(Media):
    def __init__(self,name,director,IMDB_score,url,duration,casts,count):
        super().__init__(name,director,IMDB_score,url,duration,casts)
        self.count=count
        