import os

for folder_name, sub_solders, filenames in os.walk('../../automate_boring_stuff'):
    print(f'Folder name: {folder_name}')
    if sub_solders:
        print(f'Subfolders: in {folder_name}: ')
        for subfolder in sub_solders:
            print(subfolder)
    print(f'The filenames in {folder_name}: {filenames}')
    print('-' * 40)
