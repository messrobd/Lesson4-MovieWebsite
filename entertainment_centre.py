import media
import movie_page

dredd = media.Movie("Dredd",
                    "Police officer destroys criminals",
                    "https://fanart.tv/fanart/movies/49049/movieposter/dredd-54acd03c98c8a.jpg",
                    "https://www.youtube.com/watch?v=qVIba2N6MTA")

withnail = media.Movie("Withnail and I",
                    "Eccentrics go on holiday by mistake",
                    "https://d32qys9a6wm9no.cloudfront.net/images/movies/poster/c5/c5c1cb0bebd56ae38817b251ad72bedb_500x735.jpg",
                    "https://www.youtube.com/watch?v=d9Z0DV33gAY")

movies = [dredd, withnail]

movie_page.makePage(movies)
