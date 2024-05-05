from utility import *
import pytube as pt
import os
import subprocess
from moviepy.editor import AudioFileClip
import pytube.exceptions as ptexcep
from sys import platform


# Convert a Youtube Link to an audio file (.mp3)
def convert_to_audio():
  link = input("Enter the YouTube URL to convert: ")

  # Error handling
  try:
    # Show video title and check with user whether if this is what they want to download
    video = pt.YouTube(link)
    video_name = check_name(video.title)
    print(video_name)
    print("Is this the video you want to convert?")
    user_confirm = input("Y/N: ").upper()
    
    if user_confirm == "Y":
      # Start downloading to that path with the best audio quality possible
      print("Downloading")

      # Windows file path
      file_loc = ""
      if (platform == "linux" or platform == "linux2"):
        file_loc = f"/home/{os.getlogin()}/Downloads/PyTube/"
      elif(platform == "win32"):
        file_loc = f"C:\\Users\\{os.getlogin()}\\Downloads\\PyTube\\"
      audio_stream = video.streams.get_audio_only()
      extension = audio_stream.get_file_path().split("\\")[-1].split(".")[-1]
      file_name = video_name + f".{extension}"
      audio_stream.download(file_loc, file_name)

      # Once downloaded, as the file is in .mp4 format, we will convert it into .mp3
      # Get location for input and output
      mp4_file_loc = file_loc + file_name
      mp3_file_loc = file_loc + video_name + ".mp3"
      # Convert
      audio_file = AudioFileClip(mp4_file_loc)
      audio_file.write_audiofile(mp3_file_loc)  
      audio_file.close()

      # Then, delete the mp4 file that you downloaded
      os.remove(mp4_file_loc)
      
      # Open the folder and print message once complete
      print("Convert complete, check your Downloads folder")
      subprocess.Popen(f'explorer /select,"{file_loc}"')

  # If video is unavailable
  except ptexcep.VideoUnavailable as e:
    display_error(e, "Video is Unavailable! URL Error!")

  # Any other exception that missed
  except Exception as e:
    display_error(e, "Internal Error!")

  # Print a new line, regardless whether good or not, so the new menu is separated with old stuff
  finally:
    print()
  
# Convert playlist to audio file
def convert_playlist_to_audio():
  # Get the link to the playlist
  link = input("Enter the YouTube Playlist Link: ")
  try:
    # Check if the title matches with what the playlist is
    playlist = pt.Playlist(link)
    playlist_name = check_name(playlist.title)
    print()
    print(playlist_name)
    print("Is this the playlist you want to convert?")
    user_confirm = input("Y/N: ").upper()

    # Create file path (To "Downloads/Playlist_name")
    if user_confirm == "Y":
      print("Do you want index for this playlist?")
      index_confirm = input("Y/N: ").upper()

      print("Downloading")
      if (platform == "linux" or platform == "linux2"):
        file_loc = f"/home/{os.getlogin()}/Downloads/PyTube/"
      elif(platform == "win32"):
        file_loc = f"C:\\Users\\{os.getlogin()}\\Downloads\\PyTube\\"
      folder_loc = os.path.join(file_loc, playlist_name)

      # Go through each video
      for i, video in enumerate(playlist.videos):
        # A different error handling, so that it just skips one video and not the whole playlist
        try:
          
          # Download the best resolution audio
          audio_only = video.streams.get_audio_only()
          extension = audio_only.get_file_path().split("\\")[-1].split(".")[-1]
          video_name = check_name(video.title)
          
          if index_confirm == "Y":
            file_name = f"{i+1}. {video_name}.{extension}"
          else:
            file_name = f"{video_name}.{extension}"
          # This print is for user to know that there's progress
          print(f"{i+1}.", video_name)
          audio_only.download(folder_loc, file_name)
          
          # Once finish downloading - Convert to mp4
          mp4_file_loc = os.path.join(folder_loc, file_name)
          if index_confirm == "Y":
            mp3_file_name = f"{i+1}. {video_name}.mp3"
          else:
            mp3_file_name = f"{video_name}.mp3"
          mp3_file_loc = os.path.join(folder_loc, mp3_file_name)
          # Convert
          audio_file = AudioFileClip(mp4_file_loc)
          audio_file.write_audiofile(mp3_file_loc)
          audio_file.close()
          # And removes
          os.remove(mp4_file_loc)

        # If any exception, log it out on a txt file for debugging purposes
        except Exception as e:
          print(f"Error Downloading: {i+1}. {video.title}")
          print("Video is unavailable... More information stored in 'Error.txt'")
          f = open(os.path.join(folder_loc, "Error.txt"), 'a')
          f.write(f"{os.times().user}: Video {i+1}. {video.title} can't be downloaded. Error code: {e}\n")	
          f.close()

      # Once completed, show message and open the folder
      print("Convert complete, check your Downloads folder!")
      subprocess.Popen(f'explorer /select,"{file_loc + playlist.title}"')

  # Video unavailable
  except ptexcep.VideoUnavailable as e:
    display_error(e, "Video is Unavailable! URL or Video is Privated!")

  # Any other error
  except Exception as e:
    display_error(e, "Internal Error!")

  # Print new line
  finally:
    print()
