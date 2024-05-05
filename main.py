from utility import *
from video_converter import *
from audio_converter import *

def main():
  while True:
    print("Youtube Converter")
    print("1. Convert Video to Video")
    print("2. Convert Video to Audio")
    print("3. Convert Playlist to Video")
    print("4. Convert Playlist to Audio")
    print("5. Exit")
    user_input = input("Enter your option: ")

    if user_input == "5":
      break

    elif user_input == "1":
      convert_to_video()

    elif user_input == "2":
      convert_to_audio()

    elif user_input == "3":
      convert_playlist_to_video()

    elif user_input == "4":
      convert_playlist_to_audio()

    else:
      print("Invalid Input")
      print()


if __name__ == "__main__":
  main()