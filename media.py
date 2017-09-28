import webbrowser
# Parnet Class
class Video():
    def __init__(self,title,duration):
        self.title = title
        self.duration = duration
# Child of Video
class TvShow(Video):
    def __init__(self,title,duration,season,episode):
        Video.__init__(self, title, duration)
        self.season = season
        self.episode = episode
#Child of Video and main class used for this project
class Movie(Video):
    def __init__(self,title, duration,movie_storyline,poster_image,trailer_youtube):
        Video.__init__(self, title,duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
