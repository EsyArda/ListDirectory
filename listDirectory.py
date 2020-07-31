from os import listdir, remove
from pathlib import Path


def listDirFiles(path='.'):
    """Returns the list of files and folders in a directory."""
    listDir = listdir(path)
    return sorted(listDir, key=str.lower)  # Sorted alphabetically


def listToFile(li, path='./'):
    """Creates the file 'path/liste.md' from a given list and the path."""
    try:
    	remove(path + "liste.md")
    except(FileNotFoundError):
        pass
    with open(path + "liste.md", "w", encoding="utf8") as f:
        f.write(f"# Liste des dossiers : \n`{Path().absolute()}`\n\n")
        for file in li:
            if not ("liste.md" in file or "script.py" in file):
                f.write("- " + file + "\n")
        print(f"'{path}liste.md' containing the list of files and folders was successfully created.")


listToFile(listDirFiles())

# diff /media/lilian/TOSHIBA\ EXT/Musique/liste.md liste.md -y --suppress-common-lines -w | less
