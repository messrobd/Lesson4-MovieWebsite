class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, poster_attribution, trailer_url):
        """
        1. behaviour: Constructor for Movie class
        2. inputs: string variables for movie properties:
            title
            storyline
            poster
            poster attribution
            trailer
        3. output: an instance of the Movie class, with the aforementioned
        properties
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.poster_image_attribution = poster_attribution
        self.trailer_youtube_url = trailer_url
