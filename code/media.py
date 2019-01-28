# -*- coding: cp1252 -*-
#classe video, tudo que um filme ou tvshow, precisa
class Video():
    #construtor da classe
    def __init__(self,title, duration, storyline):
        print("Video Constructor Called")
        self.title = title
        self.duration = duration
        self.storyline = storyline

#classe Visual, parte visual de um filme ou tvshow
class Visual():
    #construtor da classe
    def __init__(self, poster_image_url, trailer_youtube_url):
        print("Visual Constructor Called")
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url    


#classe de filmes
class Movie(Video,Visual):        
    def __init__(self,title, duration, storyline,poster_image_url,trailer_youtube_url,
                 release_year):
        print("Movie Constructor Called")
        Video.__init__(self,  title, duration, storyline)
        Visual.__init__(self,  poster_image_url, trailer_youtube_url)
        self.release_year = release_year
        
    #função para exibir o titulo, link e o ano de lançamento
    def show_info(self):
        print("Title - " + self.title )
        print("link_trailer - " + self.trailer_youtube_url )
        print("release_year - " + self.release_year)
    
#classe de TvShow
class TvShow(Video,Visual):        
    def __init__(self,title, duration, storyline,poster_image,trailer_youtube_url,
                 release_year):
        print("Movie Constructor Called")
        Video.__init__(self,  title, duration, storyline)
        Visual.__init__(self,  poster_image, trailer_youtube_url)
        self.release_year = release_year

    #função para exibir o titulo, link e o ano de lançamento    
    def show_info(self):
        print("Title - " + self.title )
        print("link_trailer - " + self.link_trailer )
        print("release_year - " + self.release_year)
    
