import os

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
        
#print(get_files_info("/home/aster_ray/", "workspace"))  
