from pathlib import Path

root_dir = Path('d:/python/Automation/RestAPI-Example/PathFiles/Example2/files/') #memanggil file yg otomatis akan dilakukan rename
file_paths = root_dir.glob("**/*") #glob ini digunakan untuk mencari suatu file secara keseluruhan yang ada didalam suatu direktori yang sudah dipanggil sebelumnya

for path in file_paths:
    if path.is_file():
        parent_folder = path.parts[-2] #pattern in digunakan untuk memisahkan sebuah namafile dengan karakter baru yang nanti akan ditambahkan
        new_filename =parent_folder + '-' + path.name
        print(new_filename)
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)