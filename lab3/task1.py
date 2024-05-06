import os

def check_file_access(file_path):
    return os.access(file_path, os.R_OK | os.W_OK)

file_path = input("Enter the file path: ")
access_status = check_file_access(file_path)
print("File access status:", access_status)
