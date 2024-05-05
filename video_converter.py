from utility import *

import pytube as pt
import os
import subprocess
import pytube.exceptions as ptexcep

# Function to convert one youtube link to single video
# Even if it's playlist link it will only convert one video
def convert_to_video():
  # Get link
  link = get_link()

  # Error handling
  try:
    # Show video title and check with user whether if this is what they want to download
    video = pt.YouTube(link)
    video_name = check_name(video.title)
    print(video_name)
    print("Is this the video you want to convert?")
    user_confirm = input("Y/N: ").upper()

    if user_confirm == "Y":
      # Generate the file path (To "Downloads" folder)
      if (platform == "linux" or platform == "linux2"):
        file_loc = f"/home/{os.getlogin()}/Downloads/PyTube/"
      elif(platform == "win32"):
        file_loc = f"C:\\Users\\{os.getlogin()}\\Downloads\\PyTube\\"
      # Start downloading to that path with the best resolution possible
      print("Downloading")
      best_resolution = video.streams.get_highest_resolution()
      extension = best_resolution.get_file_path().split("\\")[-1].split(".")[-1]
      file_name = video_name + f".{extension}"
      best_resolution.download(file_loc, file_name)
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
  
# Function to convert everything in playlist to video form
def convert_playlist_to_video():
  # Get the link to the playlist
  link = get_link()
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
          # Download the best resolution video
          best_resolution = video.streams.get_highest_resolution()
          extension = best_resolution.get_file_path().split("\\")[-1].split(".")[-1]
          video_name = check_name(best_resolution.title)
          file_name = f"{i+1}. {video_name}.{extension}"
          # This print is for user to know that there's progress
          print(f"{i+1}.", video_name)
          best_resolution.download(folder_loc, file_name)

        # If any exception, log it out on a txt file
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

  except Exception as e:
    display_error(e, "Internal Error")

  finally:
    print()
