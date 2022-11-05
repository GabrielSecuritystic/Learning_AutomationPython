#memasang library pathlib
from pathlib import Path

p1 = Path('d:/python/Automation/RestAPI-Example/PathFiles/introduction/files/test.txt')
#memanggil file yang akan ditampilkan datanya
print(type(p1))

if p1.exists():
    with open(p1, 'r') as file:
        print(file.read())

print(p1.name) #mencetak nama file beserta formatnya
print(p1.stem) #mencteak nama file
print(p1.suffix) #mencetak suatu format file

p2 = Path('d:/python/Automation/RestAPI-Example/PathFiles/introduction/files/coba.txt')

if not p2.exists():
    with open(p2, 'w') as file:
        file.write('coba')
