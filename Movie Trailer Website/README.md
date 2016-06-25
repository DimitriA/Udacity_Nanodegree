# entertainment_center

entertainment_center uses the [TheMovieDB](https://www.themoviedb.org/) API in order to find popular movies released in the year 2015. It then generates a website which shows movie posters (sorted by movie popularity) and allows users to view trailers. 

# Getting Started
Users will need Python. This program has been tested with Python 2.7.10; however, older versions should still be compatible. 

Second, a user should apply for and get a TheMovieDB API key. This API is free and open to use. I have provided an API key for testing purposes; however, I cannot guarantee that it will still be active.

Once you have an TMDB API key, please update the constant API_KEY in entertainment_center.py

## Command Line
    python entertainment_center.py

# What's included

**media.py** - a Movie class which stores relevant info about each movie

**entertainment_center.py** - this includes the bulk of the logic for fetching the most popular movies and their info from the TMDB API.

**fresh_tomatoes.py** - this file builds a website from the movie list passed in from entertainment_center.py. **Note:** I have modified this from the original fresh_tomatoes to handle the long dash charachter u'\u2013' present in many YouTube URLs.

# Issues
As the movie posters image files come in a variety of sizes (height and width), the page rows sometimes do not render correctly and there appear to be gaps in the poster grid. 

# License
The content of this repository is licensed under a [Creative Commons Attribution License](http://creativecommons.org/licenses/by/3.0/us/)
