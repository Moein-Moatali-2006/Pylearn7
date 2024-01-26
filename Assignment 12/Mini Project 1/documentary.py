from media import Media


class Documentary(Media):
    def __init__(self,name,director,IMDB_score,url,duration,casts,country,count):
        super().__init__(name,director,IMDB_score,url,duration,casts)
        self.country=country
        self.count=count

        