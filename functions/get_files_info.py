import os

def get_files_info(working_directory, directory="."):
  fullpath = os.path.join(working_directory, directory)
  
  absWorkingDirectory = os.path.abspath(working_directory)
  absDirectory = os.path.abspath(directory)
  print(fullpath)
  if not absDirectory.startswith(absWorkingDirectory):
    return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

  if not os.path.isdir(fullpath):
    return f'Error: "{directory}" is not a directory'
  
  result = f"Results for \"{directory}\"\n"
  for item in os.listdir(directory):
    result+=f"\t- {item}: file_size={os.path.getsize(item)} is_dir={os.path.isdir(item)}\n"

  return result

get_files_info(os.path.abspath("."))
