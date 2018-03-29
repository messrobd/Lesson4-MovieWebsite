import webbrowser
import os

"""
references:
* homebrew modal dialog code courtesy of w3schools.com
* embedded video guidance from tutorialrepublic.com
* copious assistance w3schools and stackoverflow to get my javascript to work
"""

page_layout = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Rob's movies</title>
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <div class="header">
        <h1>Rob's movies</h1>
    </div>
    <div class="movie-list">{movie_tiles}</div>
    <div id="modal">
      <div id="player-container">
        <div>
          <span id="dismissPlayerControl">&times;</a>
        </div>
        <div>
          <iframe id="player" width="560" height="315" src="" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
        </div>
      </div>
    </div>
    <script>{script}</script>
  </body>
</html>
"""

movie_tile = """
<div class="movie-tile">
    <div id="{movie_title}" class="image-container">
        <img class="movie-image" src="{poster_image_url}">
    </div>
    <div class="attribution">
        <p class="attribution-text">{poster_image_attribution}</p>
    </div>
    <h2 class="title-container">{movie_title}</h2>
</div>
"""

script = """
      var modalElement = document.getElementById('modal');
      var playerElement = document.getElementById('player');

      function invokePlayer(trailerURL){{
        playerElement.src = trailerURL
        modalElement.style.display = 'flex'
      }}
      function dismissPlayer(){{
        modalElement.style.display = 'none'
        playerElement.src = ''
      }}

      function makeInvokeHandler(trailerURL) {{
        return function () {{
          invokePlayer(trailerURL);
        }}
      }}

      var trailerDict = {trailerDict};

      for (var movie in trailerDict) {{
        var movieTile = document.getElementById(movie);
        var trailerURL = trailerDict[movie];
        movieTile.onclick = makeInvokeHandler(trailerURL);
      }}

      var dismissPlayerControl = document.getElementById('dismissPlayerControl');
      dismissPlayerControl.onclick = dismissPlayer;
"""

def makeTiles(movies):
    """
    1. behaviour: produces a tailored html fragment for each movie in a list
    2. input:
       i. a list containing instances of the movie class
       ii. an html fragment as a string defining the structure of the movie
       element, in which variables stand in for movie properties to be populated
    3. output: html as a string, subsituting movie instance properties for
    variables in the input string
    """
    movie_tiles = ""
    for movie in movies:
        movie_tiles += movie_tile.format(
        movie_title = movie.title,
        poster_image_url = movie.poster_image_url,
        poster_image_attribution = movie.poster_image_attribution,
        )

    return movie_tiles

def makeEmbedURL(trailer_youtube_url):
    """
    1. behaviour: converts a youtube "watch" url into a youtube "embed" url
    2. input: a youtube "watch" url
    3. output: a youtube "embed" url
    """
    parts_to_keep = trailer_youtube_url.split("watch?v=")

    youtube_base_url_index = 0
    youtube_video_id_index = 1

    embed_url = "{0}embed/{1}".format(
        parts_to_keep[youtube_base_url_index],
        parts_to_keep[youtube_video_id_index]
        )

    return embed_url

def makeScript(movies):
    """
    1. behaviour: generates a javascript component to control a modal player
    element on the page
    2. inputs:
       i. a list containing instances of the movie class
       ii. a javascript fragment as a string, in which a variable stands in for
       the dictionary of trailer url's to be substituted
    3. output: javascript as a string. the javascript sets up event handlers for
    each movie tile element, such that it will invoke a modal youtube player
    dialog for the associated trailer video
    """
    trailerDict = {}
    for movie in movies:
        movieID = movie.title
        trailerURL = makeEmbedURL(movie.trailer_youtube_url)
        trailerDict[movieID] = trailerURL

    return script.format(trailerDict = str(trailerDict))

def makePage(movies):
    """
    1. behaviour: creates and opens an html file incorporating a set of movie
    elements
    2. inputs:
       i. a list containing instances of the movie class
       ii. an html fragment as a string defining the structure of the web page,
       in which a variable stands in for the movie list html to be substituted
       iii. a javascript fragment to control a modal player element on the page
    3. outputs: an html file substituting movie list html and script elements
    into the input html string
    """
    initial_working_dir = os.getcwd()
    project_folder = os.path.dirname(__file__)
    os.chdir(project_folder)

    movie_webpage_file = open("movie_webpage.html", "w")

    composed_page = page_layout.format(movie_tiles = makeTiles(movies), script = makeScript(movies))

    movie_webpage_file.write(composed_page)
    movie_webpage_file.close()

    url = os.path.abspath(movie_webpage_file.name)
    webbrowser.open("file://"+url)

    os.chdir(initial_working_dir)
