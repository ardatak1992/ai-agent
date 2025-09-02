import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
  absWorkingDirectory = os.path.abspath(working_directory)
  fullpath = os.path.abspath(os.path.join(absWorkingDirectory, file_path))
  print(fullpath)
  
  if not fullpath.startswith(absWorkingDirectory):
    return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

  if not os.path.exists(fullpath):
    return f'Error: File "{file_path}" not found.'

  if not fullpath.endswith(".py"):
    return f'Error: "{file_path}" is not a Python file.'


  if not os.path.isfile(fullpath):
    return f'Error: "{file_path}" is not a file'
  
  
    
