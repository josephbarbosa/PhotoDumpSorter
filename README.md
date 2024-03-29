# Photo Dump Sorter

A huge present issue for photographers today is the time it takes for them to sort out and go through photos directly following a shoot. Many photographers take "burst" photos at each click of the button, often consisting of 20 photos per "shot". This often results in a large photo dump following the shoot where the photographer must sit and sort through the acceptable photos that he/she will select for editing and potentially shipping back to the client. The photographer loses this valuable time doing this task which could be used on editing.

This script is designed to help with that dilemma and does the preliminary sorting out for you! This is a short python script that analyzes a folder photo-by-photo to decide whether or not the selected photo should be selected to be a candidate. The python script does this by analyzing the sharpness value per photo and selecting the ones that is above a given threshold. The python script uses the SightEngine API to analyze each photo and separates the "good" and the "bad" photos into their respective folders.

# How To Use It
1. Make sure you have the latest version of python installed. https://www.python.org/downloads/ (Python 3+) <br />
2. Open up a terminal/command prompt and run command `pip3 install sightengine` <br />
3. Open up the script file in notepad or sublime text and change `root_dir` to where the file where the photos are located are. <br />
4. Change the threshold value based on how sensitive you want the system to be. 0.95 more often is a good value. The closer to 1 it is, the less blurry of a picture it will be categorized as 'good'. <br />
5. Visit https://sightengine.com/ and create an account. <br />
6. After logging in select `Account` tab, copy and paste the API_USER and API_SECRET fields and change the values `api_user_id` and `api_key` inside the PYTHON SCRIPT accordingly. <br />
7. Run the script using the command `python3 sharp.py`on MacOS or `python sharp.py` on Windows. <br />
8. The script should create logs of the pre-analyzed photo dump with its image and its sharpness value, as well as the post-analyzed log. <br />
9. "GOOD" images will be stored in the Analyzed_Images folder. "BAD" images will be stored in the "Under_Threshold" folder. <br />

# TODO / Future Changes
1. Currently only supports MacOS, working on Windows version.
2. Will add GUI support to make it more user-friendly.
