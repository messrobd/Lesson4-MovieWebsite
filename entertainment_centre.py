import media
import movie_page

dredd = media.Movie("Dredd",
                    "Future police officer kills criminals",
                    "https://upload.wikimedia.org/wikipedia/en/1/16/Dredd2012Poster.jpg",
                    "https://www.youtube.com/watch?v=qVIba2N6MTA")

withnail = media.Movie("Withnail and I",
                    "Eccentrics go on holiday by mistake",
                    "https://upload.wikimedia.org/wikipedia/en/f/fe/Withnail_and_i_poster.jpg",
                    "https://www.youtube.com/watch?v=d9Z0DV33gAY")

aliens = media.Movie("Aliens",
                    "Hideous creature kills everyone",
                    "https://upload.wikimedia.org/wikipedia/en/f/fb/Aliens_poster.jpg",
                    "https://www.youtube.com/watch?v=XKSQmYUaIyE")

lotr = media.Movie("Lord of the Rings",
                    "Little guy destroys evil wizard",
                    "https://upload.wikimedia.org/wikipedia/en/8/87/Ringstrilogyposter.jpg",
                    "https://www.youtube.com/watch?v=V75dMMIW2B4")

american_beauty = media.Movie("American Beauty",
                    "Middle class man rebels against stereotype",
                    "https://upload.wikimedia.org/wikipedia/en/b/b6/American_Beauty_poster.jpg",
                    "https://www.youtube.com/watch?v=Ly7rq5EsTC8")

empire = media.Movie("Star Wars: The Empire Strikes Back",
                    "Underdogs don't defeat evil space empire",
                    "https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
                    "https://www.youtube.com/watch?v=mz_YWNhKOkM")

movies = [
    dredd,
    withnail,
    aliens,
    lotr,
    american_beauty,
    empire]

movie_page.makePage(movies)
