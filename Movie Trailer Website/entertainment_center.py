import fresh_tomatoes
import json
import media
import urllib

TMDB_NEW_RELEASES_QUERY = "https://api.themoviedb.org/3/discover/movie?primary_release_date.gte=2015-01-01&primary_release_date.lte=2015-12-31"  # NOQA
TMDB_MOVIE_INFO_QUERY = "https://api.themoviedb.org/3/movie/%d?append_to_response=trailers"  # NOQA
API_KEY = "&api_key=INSERT_API_KEYH_HERE"
POSTER_BASE_URL = "http://image.tmdb.org/t/p/w300/"
YOUTUBE_BASE_URL = "https://www.youtube.com/watch?v="

# Fetching info on new releases this year
tmdb_connection = urllib.urlopen(TMDB_NEW_RELEASES_QUERY + API_KEY)
new_releases_response = tmdb_connection.read()
tmdb_connection.close()
new_releases_json = json.loads(new_releases_response)

movies = []
for movie in new_releases_json["results"]:
	# Fetching additional info for each movie
	tmdb_connection = urllib.urlopen((TMDB_MOVIE_INFO_QUERY % movie["id"]) +
									  API_KEY)
	movie_response = tmdb_connection.read()
	tmdb_connection.close()
	movie_info_json = json.loads(movie_response)

	temp = media.Movie(movie_info_json["original_title"],
					   movie_info_json["overview"],
					   (POSTER_BASE_URL + movie_info_json["poster_path"]),
					   (YOUTUBE_BASE_URL +
					   	movie_info_json["trailers"]["youtube"][0]["source"]))
	movies.append(temp)

fresh_tomatoes.open_movies_page(movies)

