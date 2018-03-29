import media
import movie_page

test_movie = media.Movie("title", "storyline", "poster", "attribution", "trailer")

assert test_movie.title == "title"
assert test_movie.storyline == "storyline"
assert test_movie.poster_image_url == "poster"
assert test_movie.trailer_youtube_url == "trailer"

test_html = """<a href="{trailer_youtube_url}" target="_blank">"""

assert test_html.format(
    trailer_youtube_url = test_movie.trailer_youtube_url
    ) == """<a href="trailer" target="_blank">"""

test_trailer_url = "https://www.youtube.com/watch?v=d9Z0DV33gAY"

print movie_page.makeEmbedURL(test_trailer_url)

print "ran all tests"
