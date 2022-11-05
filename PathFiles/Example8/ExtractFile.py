from pathlib import Path
import zipfile


root_dir = Path('d:/python/Automation/RestAPI-Example/PathFiles/Example8')
destination_path = Path('d:/python/Automation/RestAPI-Example/PathFiles/Example8/files/') #direktori tujuan untuk tempat extract file

for path in root_dir.glob("*.zip"):
    with zipfile.ZipFile(path,'r') as zf:
        final_path = destination_path / Path(path.stem)
        zf.extractall(path=final_path) #fungsi ini digunakan untuk mengekstrak suatu file

