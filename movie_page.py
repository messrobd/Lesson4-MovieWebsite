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
    <a> href="{trailer_youtube_id}"
        <img class="movie-image" src="{poster_image_url}">
    </a>
    <h2>{movie_title}</h2>
</div>
"""

def makeTiles(movies, movie_tile):
    movie_tiles = ""
    for movie in movies:
        movie_tile.format(
        trailer_youtube_id = movie.trailer_youtube_id,
        poster_image_url = movie.poster,
        movie_title = movie.movie_title
        )
        movie_tiles += movie_tile

    return movie_tiles
