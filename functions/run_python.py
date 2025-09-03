import os
import subprocess
from google.genai import types

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
  
  completeArgs = ["python3", fullpath] + args

  try:
    pr= subprocess.run(args=completeArgs, timeout=30, capture_output=True )
    if (pr.returncode != 0):
      return f"STDOUT: Process exited with code {pr.returncode}"
    elif (len(pr.stdout) == 0):
      return f"STDOUT: No output produced."
    else:
      return f"STDOUT: ${pr.stdout}"
  except Exception as e:
      return f"Error: executing Python file: {e}"



schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs python file with additional arguments.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path of the file relative to working directory",
            ),
        },
    ),
)

