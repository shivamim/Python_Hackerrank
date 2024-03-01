#TASK 
'''Check file is empty or not'''

#SOLUTION 

import os

file_path = 'your_file.txt'  # Replace 'your_file.txt' with the actual file path

file_size = os.stat(file_path).st_size

if file_size == 0:
    print(f"The file {file_path} is empty.")
else:
    print(f"The file {file_path} is not empty. Size: {file_size} bytes.")
