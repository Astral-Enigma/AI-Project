import os
import subprocess

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
        return f"Error: executing Python file: {e}"