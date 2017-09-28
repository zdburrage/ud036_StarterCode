import media
import fresh_tomatoes

"""Here, 6 movies are initialized by passing their corresponding
properties into a constructor
(title, duration, storyline, poster art, and youtube url).
Each object is initialized as
media.Movie() which references the media file and the Movie
class"""
toy_story = media.Movie("Toy Story", "1:21:00",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/" +
                        "wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
superbad = media.Movie("Superbad", "1:53:00",
                       "Two friends go on a quest to have" +
                       "an awesome time at a party before they graduate",
                       "http://www.cinemasterpieces.com/superbadjan08.jpg",
                       "https://www.youtube.com/watch?v=G05Xdl5eGqo")
django = media.Movie("Django: Unchained", "2:45:00",
                     "A slave escapes from his owner and rescues" +
                     "his wife whom he hasn't seen in years",
                     "http://www.heyuguys.com/images" +
                     "/2012/10/Django-Unchained-International-Poster.jpg",
                     "https://www.youtube.com/watch?v=eUdM9vrCbow")
ily_man = media.Movie("I Love You, Man", "1:45:00",
                      "A man struggling to find male friends meets an" +
                      "instant" +
                      "BFF right before he and his wife get married",
                      "https://www.movieposter.com/posters/archive" +
                      "/main/80/MPW-40339",
                      "https://www.youtube.com/watch?v=um5DuTLzw-I")
the_big_short = media.Movie("The Big Short", "2:10:00",
                            "Three groups of people discover the American" +
                            "Housing" +
                            "Crisis before it happens, and profit big on it.",
                            "http://cdn.film-book.com/wp-content/uploads" +
                            "/2015/11/the-big-short-movie-poster-01.png",
                            "https://www.youtube.com/watch?v=vgqG3ITMv1Q")
a_walk_to_remember = media.Movie("A Walk to Remember", "1:42:00",
                                 "A jaded, aimless high school senior" +
                                 "(Shane West) who falls in love" +
                                 "with a guileless young woman" +
                                 "(Mandy Moore)" +
                                 "he and his friends once scorned",
                                 "https://images-na.ssl-images-amazon.com" +
                                 "/images/I/51TKV2HF1TL._SY445_.jpg",
                                 "https://www.youtube.com/watch?v=EgdoQ8Oxu2E")

"""This gathers all of the movies initialized above and puts
them into a list"""
movies = [toy_story, superbad, django, ily_man,
          the_big_short, a_walk_to_remember]

"""This function references the open_movies_page function from the
fresh_tomatoes.py file and passes in the above created list of
movies. This will create the web page and fill it with the
appropriate movie data"""
fresh_tomatoes.open_movies_page(movies)


