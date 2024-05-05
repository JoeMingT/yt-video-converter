

# To replace illegal characters for file naming in Windows 11 with nothing
def check_name(name):
  NOT_ALLOWED = ["\\", "/", ":", "*" ,"?", '"', "<", ">", "|"]

  new_name = name
  for char in NOT_ALLOWED:
    new_name = new_name.replace(char, "")
  
  return new_name


def display_error(error, error_message):
  print(error)
  print(error_message)


def get_link():
  return input("Enter the YouTube URL Link: ")