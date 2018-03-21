import webbrowser

class Movie(): #capitalisation per google sytle guide
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_url): #__init__ is a built-in function. self refers to the instance
        #all these attributes must be provided when the class is instantiated
        #they become instance variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_url

    def showTrailer(self):
        webbrowser.open(self.trailer)
