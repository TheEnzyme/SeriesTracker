# Series Tracker

A simple script to parse html files from TVRage.com and get a list of episodes
for a given TV Show.

## Usage

As of this version, the series title is hardcoded on the main function, but
it must be easy extend the code and create a list of series names and
episodes.

## Long delays

It takes a html fetch action to get each episode synopsis, so for long running
series, the fetching process might take a while. To avoid synopsis fetching,
it's only necessary to set SYNOPSIS to False.

## TODO
* Better output formatting
* Add local content to compare against.
* Cache synopsis' to increase script speed.
* Config file(s) to input shows and settings.
* User friendly terminal interface.
* Seperate terminal interface into a wrapper
* Wrapper for inputting and creating config file
* Bundle into pip package to take care of dependencies
* Fake HTML formatted output, to make parsing not increase dependencies