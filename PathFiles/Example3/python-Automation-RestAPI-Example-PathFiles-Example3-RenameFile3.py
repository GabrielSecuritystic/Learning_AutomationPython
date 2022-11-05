#Example RenameFile on SubFolders

from pathlib import Path

root_dir = Path('d:/python/Automation/RestAPI-Example/PathFiles/Example3/file-1') #memanggil file yg otomatis akan dilakukan rename

for path in root_dir.glob("**/*"):
    if path.is_file():
        parent_folder = path.parts
        subfolders = path.parts[1:-1]
        new_filename = "-".join(subfolders)+'-'+path.name
        print(new_filename)
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)