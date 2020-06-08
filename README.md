# Python Turtle Drawer

This is a simple python script that creates paths consisting of forward motion and left, right. 

This is used to generate maps for a lesson I am developing for elementary students using [BeeBots](https://www.terrapinlogo.com/).
Each student will be given a bot and figure out how to make it traverse from start to finish by programming forward, left, and right commands.

## How to Run
This script can work in either the console/terminal window or as a stand-alone app. 

To use in the terminal, use the command:

`python3 path_maker.py`

To use as a stand-alone app, just double click `path_maker.py`.

This requires that Python 3 is installed on the computer. Saving the images also requires [Pillow](https://python-pillow.org/).

## How to change the parameters

If you would like to change the length of each difficulty level (Beginner, Intermediate, Advanced) or even add new difficulty levels, change the values in the dictionary variable `type_of_paths` in the main function of `path_maker.py`.

To change how many of each type of path are generated, adjust `number_of_each_type`, also in the main function