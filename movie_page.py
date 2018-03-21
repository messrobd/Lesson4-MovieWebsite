import webbrowser
import os

page_layout = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Rob's movies</title>
  </head>
  <body>
    <div class="header"></div>
    <div class="movie-list">{movie_tiles}</div>
  </body>
</html>
"""

movie_tile = """
<div class="movie-tile">
    <a href="{trailer_youtube_url}" target="_blank">
        <img class="movie-image" src="{poster_image_url}">
    </a>
    <h2>{movie_title}</h2>
</div>
"""

def makeTiles(movies):
    movie_tiles = ""
    for movie in movies:
        movie_tiles += movie_tile.format(
        trailer_youtube_url = movie.trailer_youtube_url,
        poster_image_url = movie.poster_image_url,
        movie_title = movie.title
        )

    return movie_tiles

def makePage(movies):
    movie_webpage_file = open("movie_webpage.html", "w")

    composed_page = page_layout.format(movie_tiles = makeTiles(movies))

    movie_webpage_file.write(composed_page)
    movie_webpage_file.close()

    url = os.path.abspath(movie_webpage_file.name)
    webbrowser.open("file://"+url)
