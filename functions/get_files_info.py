import os
from google.genai import types

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


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
