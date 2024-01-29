import pytube

class Media:
    def __init__(self,name,director,IMDB_score,url,duration,casts):
        self.name=name
        self.director=director
        self.IMDB=IMDB_score
        self.url=url
        self.duration=duration
        self.casts=casts

    @staticmethod
    def showinfo():
        ...
        
    @staticmethod
    def download():
        link=input("Please import link: ")
        first_stream=pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./',filename='video.mp4')
        print("downloaded and saved")