#Menambahkan tanggal pembuatan suatu file

from pathlib import Path
from datetime import datetime
import os

root_dir = Path('d:/python/Automation/RestAPI-Example/PathFiles/Example4/files/') #memanggil file yg otomatis akan dilakukan rename

for path in root_dir.glob("**/*"):
  if path.is_file():
    created_date = datetime.fromtimestamp(path.stat().st_ctime)
    created_date_str = created_date.strftime("%Y-%m-%d %H:%M:%S")
    new_filename = created_date_str + '_' + path.name
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)