from pathlib import Path

root_dir = Path('d:/python/Automation/RestAPI-Example/PathFiles/Example9/files')
search_term = 'test' #mencari file yg memiliki nama test

for path in root_dir.rglob("*"):
    if path.is_file():
        if search_term in path.stem:
            print(path.absolute())