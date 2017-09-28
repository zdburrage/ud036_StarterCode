import webbrowser


class Video():
    """The Parent class for Movie and TvShow. This hold the properties
    and initialization function for title and duration. Takes two
    arguments to initialize (title and duration) both of type
    string and can be called from a child class"""
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class TvShow(Video):
    """This is a child class of Video that inherits its properties title
    and duration. Its __init__ function calls the Video __init__ function
    which sets the title and duration. Its(TvShow's) __init__ function
    also sets the properties season and episode for the object equal
    to the values passed in"""
    def __init__(self, title, duration, season, episode):
        Video.__init__(self, title, duration)
        self.season = season
        self.episode = episode


class Movie(Video):
    """The main class used for this project and a child class of video.
    Inherits the properties title and duration from Video. Its
    __init__ function calls Video's __init__ function to set
    the above mentioned properties. The other peoperties passed in
    (movie_storyline, poster_image, and trailer_youtube) are
    set below the video __init__ call, made equal to the values
    passed in."""
    def __init__(self, title, duration, movie_storyline,
                 poster_image, trailer_youtube):
        Video.__init__(self, title, duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """This function uses the webbrowser library to access
        a web page with the object's current value in the
        trailer_youtube_url field, which would ideally
        go to youtube and play the trailer of the
        desired movie"""
        webbrowser.open(self.trailer_youtube_url)
