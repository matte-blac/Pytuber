# Pytuber

## Description
This project is a Youtube Playlist Downloader, a Python application that allows users to download all videos from a given YouTube playlist. The application provides a user-friendly interface where users can enter the URL of the playlist they want to download.

## Tech Stack
This application is built with Python and uses several libraries:
- `tkinter` for the graphical user interface
- `pyyoutube` to interact  with YouTube's API
- `pytube` to download Youtube videos
- `threading` to improve the application's performance by allowing simultaneous downloads

## Design
The application runs in a window and provides a simple and intuitive interface. Users can enter the URL of the playlist they want to download, view the list of videos in the playlist and start the download process with a single click.

## Features
- Download all videos from a YouTube playlist
- View the list of videos in playlist
- Select multiple videos to download
- Download videos in the highest available resolution

## Getting Started
1. Clone this repository using git or download it as a zip file
2. Install the required Python libraries (`pip install pyyoutube pytube3 tkinter`)
3. Run the application (`python main.py`)
4. Enter the URL of the YouTube playlist you want to download
5. Click 'Get Videos' to fetch the list of videos
6. Select the videos you want to download
7. Click 'Start Download' to start the downloading process