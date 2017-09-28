*This is written in Python 3.6.2*
Author: Zachary Burrage, zb427q@att.com

Project Description: The first Udacity Full Stack Nanodegree project. This small project generates an HTML page with a list of movies and links to their trailers, making use of classes and objects as well as list to generate the website.

There are three main files:

entertainment_center.py - Initializes/constructs each movie by calling the movie constructor and loading it with the appropriate data. In this case - title, duration, storyline, poster art, and youtube trailer link. After initializing the movies it loads all of the movies into a list and calles the open_movies_page() function in fresh_tomatoes.py which loads a web page based on the data of the movies in the given list.

media.py - contains the class definitions for Video - the parent class, as well as Movie and TvShow which are child classes of Video and inherit the properties "title" and "duration" from Video.

fresh_tomatoes.py - contains all of the HTML, JavaScript, and CSS for the page based on the data given to its function "open_movies_page(movies)" where movies is a list of movie objects passed from entertainment_center.py

In order to run the program:

IF CLONING REPOSITORY:
1. If you don't have Git installed, download it at https://git-scm.com/downloads
2. Open a command window or Git Bash
3. Navigate to a directory that you would like to clone the repository into by typing "cd <File Location>" to step further in a directory or "cd.." to step back in the file tree
4. When you are in the desired location, type "git clone https://github.com/zdburrage/ud036_StarterCode.git"
5. If the repository cloned successfully, follow steps 5-9 of below directions

IF DOWNLOADING ZIP FILE:
1. Go to https://github.com/zdburrage/ud036_StarterCode
2. Click 'Clone or download'
3. Click 'Download Zip'
4. After the repository is downloaded, extract/save it to a file location of your choosing
5. If you have Python and IDLE installed, search for IDLE in all programs and open it. Else, download Python at https://www.python.org/downloads/ and install Python
6. When you have IDLE open, click 'File' and then 'Open'
7. Navigate to the file path where you extracted the repository, find 'entertainment_center.py', click on it
8. Click 'Open' to open the file in IDLE
9. Finally, click 'Run' then 'Run Module' and the file will open a local web page!

TO GET LATEST VERSION OF CODE:
1. Open a command window
2. Navigate to the file directory where your repository is kept
3. Enter the command 'git pull' and you will have the latest code, assuming there are no merge conflicts



