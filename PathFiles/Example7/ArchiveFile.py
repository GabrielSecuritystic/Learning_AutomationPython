#membuat program archive file kedalam bentuk ZIP
from pathlib import Path
import zipfile

root_dir = Path('d:/python/Automation/RestAPI-Example/PathFiles/Example7/files/')
archive_path = root_dir / Path('archive.zip')

with zipfile.ZipFile(archive_path, 'w') as zf:
  for path in root_dir.rglob("*.txt"):
    zf.write(path)
    path.unlink()
