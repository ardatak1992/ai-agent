import os
from google.genai import types

def write_file(working_directory, file_path, content):
  absWorkingDirectory = os.path.abspath(working_directory)
  fullpath = os.path.abspath(os.path.join(absWorkingDirectory, file_path))
  head, _ = os.path.split(fullpath)

  if not fullpath.startswith(absWorkingDirectory):
    return f'Error: Cannot write to "{fullpath}" as it is outside the permitted working directory'

  if not os.path.exists(head):
    os.makedirs(head)

  try:
    with open(fullpath, "w") as f:
      f.write(content)
      return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
  except Exception as e:
    return "Error: cannot write to file {e}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Runs python file with additional arguments.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path of the file relative to working directory",
            ),
            "content": types.Schema(
              type= types.Type.STRING,
              description="The text you write to the file"
            )
        },
    ),
)
