from pathlib import Path

root_dir = Path('d:/python/Automation/RestAPI-Example/PathFiles/Example10/files')

for path in root_dir.glob("*.txt"): #memanggil semua file yang berformat .txt
    with open(path,'wb') as file:
        file.write(b'')
        path.unlink()