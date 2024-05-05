# yt-video-converter
This application is a Command Line Interface that allows you to convert most public YouTube link to video (.mp4) or audio (.mp3) format. Limited but straightforward. Currently, there's no implementation for saving metadata, choosing file extensions and so on. It's something I cooked up very fast back then.

<br>

## Libraries Used
The application uses a few libraries to run this properly. The libraries are:

1. [pytube](https://github.com/pytube/pytube) (Main library used to fetch YT data from URL provided)
2. [moviepy](https://github.com/Zulko/moviepy) (Library used to convert to mp3 file format)

<br>

## How to Run
First, make sure you have Python 3.9 and above installed in your computer:
```cmd
python --version
```

Then, install the necessary dependencies / libraries:
```cmd
pip install pytube moviepy
```

Finally, run the `main.py` file using Python
```
python main.py
```

<br>

#### Note
Me and this application take no responsibility in what you convert. Please make sure that you have the permission / rights to convert the video before converting.