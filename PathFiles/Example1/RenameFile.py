from pathlib import Path

root_dir = Path('d:/python/Automation/RestAPI-Example/PathFiles/Example1/files/') #memanggil file yg otomatis akan dilakukan rename
file_paths = root_dir.iterdir() #fungsi iterdir ini mengembalikan nilai true jika file yang dipanggil sebelumnya memang ada disuatu direktori
print(Path.cwd()) #ini akan me return/mengembalikan object dimana berisi jalur yang mewakili direktori yang saat ini sedang digunakan
for path in file_paths:
  new_filename = "new-" + path.stem + path.suffix #menambahkan keyword new sebelum nama file yang sebelumnya pernah dibuat
  new_filepath = path.with_name(new_filename)
  print(new_filepath) #mencetak hasil rename suatu file tersebut
  path.rename(new_filepath) #rename suatu file

