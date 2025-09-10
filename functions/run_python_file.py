import os
import subprocess
<<<<<<< HEAD
from google import genai
=======
>>>>>>> 98d8511 (Run_python_AI)

def run_python_file(working_directory, file_path, args=[]):
    working_directory = os.path.abspath(working_directory)
    full_path = os.path.join(working_directory, file_path)
    abs_path = os.path.abspath(full_path)

    if not abs_path.startswith(working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory' 
    
    if not os.path.isfile(abs_path):
        return f'Error: File "{file_path}" not found.'
    
    if not abs_path.endswith("py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    commands = ["python", abs_path]
    if args:
        commands.extend(args)

    try:
        completed_process = subprocess.run(commands, text=True, timeout=30, capture_output=True, cwd= working_directory)
        output = ""
        if completed_process.stdout:
            output += f"STDOUT: {completed_process.stdout}"

        if completed_process.stderr:
            output+= f"STDERR: {completed_process.stderr}"

        if completed_process.returncode != 0:
            output += f"Process exited with code {completed_process.returncode}"  

        if output == "":
            return "No output produced."
        
        return output
     
    except Exception as e:
<<<<<<< HEAD
        return f"Error: executing Python file: {e}"
    

schema_run_python_file = genai.types.FunctionDeclaration(
name="run_python_file",
description="Executes a Python file within the working directory and returns the output from the interpreter.",
parameters= genai.types.Schema(
    type= genai.types.Type.OBJECT,
    properties={
        "file_path": genai.types.Schema(
            type= genai.types.Type.STRING,
            description="Path to the Python file to execute, relative to the working directory.",
        ),
        "args": genai.types.Schema(
            type= genai.types.Type.ARRAY,
            items= genai.types.Schema(
                type= genai.types.Type.STRING,
                description= "Optional arguments to pass to the Python file.",
            ),
            description="Optional arguments to pass to the Python file.",
        ),
    },
    required=["file_path"],
),
)
=======
        return f"Error: executing Python file: {e}"
>>>>>>> 98d8511 (Run_python_AI)
