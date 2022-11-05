from pathlib import Path


root_dir = Path('d:/python/Automation/RestAPI-Example/PathFiles/Example5/files/')

for path in root_dir.rglob("*.txt"): #mengubah format file yg sudah ada didalam direktori yg dipanggil sebelumnya
    if path.is_file():
        new_filepath =path.with_suffix(".py") #mengubah format file yg sudah ada didalam direktori yg dipanggil sebelumnya menjadi format .py
        path.rename(new_filepath)