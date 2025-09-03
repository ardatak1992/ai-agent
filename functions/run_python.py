import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):

  absWorkingDirectory = os.path.abspath(working_directory)
  fullpath = os.path.abspath(os.path.join(working_directory, file_path))
  print(fullpath)
  
  if not fullpath.startswith(absWorkingDirectory):
    return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

  if not os.path.exists(fullpath):
    return f'Error: File "{file_path}" not found.'

  if not file_path.endswith(".py"):
    return f'Error: "{file_path}" is not a Python file.'

  try:
    completeArgs = ["python", fullpath]
    if (args):
      completeArgs.extend(args)
    print(completeArgs)
    res= subprocess.run(
        completeArgs, 
        timeout=30,
        text=True,
        capture_output=True,
        cwd= absWorkingDirectory
        )

    output = []
    if (res.returncode != 0):
      output.append(f"Process exited with code {res.returncode}")
    if res.stdout:
      output.append(f"STDOUT\n: Process exited with code {res.stdout}")
    if res.stderr:
      output.append(f"STDERR:\n{res.stderr}")
    
    return "\n".join(output) if output else "No output produced."
  except Exception as e:
    return f"Error: executing Python file: {e}"


print(run_python_file("./calculator", "tests.py"))


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

