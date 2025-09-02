import os

def get_files_info(working_directory, directory="."):
  
  
  absWorkingDirectory = os.path.abspath(working_directory)
  fullpath = os.path.abspath(os.path.join(absWorkingDirectory, directory))
  
  if not fullpath.startswith(absWorkingDirectory):
    return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'


  if not os.path.isdir(fullpath):
    return f'Error: "{directory}" is not a directory'
  
  try:
    result = f"Results for \"{directory}\"\n"
    for item in os.listdir(fullpath):
      filePath = f"{fullpath}/{item}"
      size = os.path.getsize(filePath)
      isDir = os.path.isdir(filePath)
      result+=f"\t- {item}: file_size={size} bytes, is_dir={isDir}\n"
    return result
  except Exception as e:
    return f"Error listing files: {e}"


get_files_info(".", "../")
