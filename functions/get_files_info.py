import os
from google import genai

def get_files_info(working_directory, directory="."):
    working_directory = os.path.abspath(working_directory)
    full_path = os.path.join(working_directory, directory)
    abs_path = os.path.abspath(full_path)


    if not abs_path.startswith(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(abs_path):
        return f'Error: "{directory}" is not a directory'
    
    output = ""

    for file in os.listdir(abs_path):
        path = os.path.join(abs_path, file)
        output += f"- {file}: file_size={os.path.getsize(path)} bytes, is_dir={os.path.isdir(path)}\n"
    return output
        

schema_get_files_info = genai.types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "directory": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

