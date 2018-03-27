import media

test_movie = media.Movie("title", "storyline", "poster", "trailer")

assert test_movie.title == "title"
assert test_movie.storyline == "storyline"
assert test_movie.poster_image_url == "poster"
assert test_movie.trailer_youtube_url == "trailer"

test_html = """<a href="{trailer_youtube_url}" target="_blank">"""

assert test_html.format(
    trailer_youtube_url = test_movie.trailer_youtube_url
    ) == """<a href="trailer" target="_blank">"""

print "ran all tests"
