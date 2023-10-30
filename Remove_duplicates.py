import os
def list_files(starting_directory):
    seen_files = set()
    duplicate_files = []
    for root, _, files in os.walk(starting_directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file in seen_files:
                duplicate_files.append(file_path)
            else:
                seen_files.add(file)
    return duplicate_files
duplicate_files = list_files(r'D:\Kabali_da')
for file_path in duplicate_files:
    if os.path.exists(file_path):
        os.remove(file_path)
        print(8*'\n')
        print(file_path)        
        print(8*'\n')
    else:
        print(f"File '{file_path}' does not exist or cannot be deleted.")