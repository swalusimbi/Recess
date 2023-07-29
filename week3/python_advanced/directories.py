""" 
DIRECTORY HANDLING.
Involves working with directories (folders) in the file system. 
Python provides modules like os and shutil that offer various functions and methods to perform directory-related operations. 
"""
import os, shutil

def create_directory(directory_path):
    os.mkdir(directory_path)
    print(f"Directory '{directory_path}' created successfully.")

def remove_directory(directory_path):
    os.rmdir(directory_path)
    print(f"Directory '{directory_path}' removed successfully.")

def list_directory(directory_path):
    content = os.listdir(directory_path)
    print(f"Contents of directory '{directory_path}':")
    for file in content:
        print(file)

def check_directory_exists(directory_path):
    if os.path.exists(directory_path):
        print(f"Directory '{directory_path}' exists.")
    else:
        print(f"Directory '{directory_path}' does not exist.")

def delete_directory(directory_path):
    try:
        shutil.rmtree(directory_path)
        print(f"Directory '{directory_path}' deleted successfully.")
    except FileNotFoundError:
        print(f"Directory '{directory_path}' does not exist.")
    except OSError as e:
        print(f"Error occurred while deleting directory '{directory_path}': {str(e)}")

def CWD():
    cwd = os.getcwd()
    print("Current directory:", cwd)

if __name__ == "__main__":
    # Call the functions
    directory_path = "folder2" 
    non_empty_dire = "folder1"
    CWD()
    # create_directory(directory_path)
    # check_directory_exists(directory_path)
    # list_directory(directory_path)
    # remove_directory(directory_path)  # .. only empty directories
    # delete_directory(non_empty_dire)
    