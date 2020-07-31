from os import listdir, remove, path, walk
from os.path import isfile, isdir
from pathlib import Path


def listDirFiles(pathDir='./'):
    """Returns the list of files and folders in a directory."""
    listDir = listdir(pathDir)
    # print("list : ", listDir)
    return sorted(listDir, key=str.lower)  # Sorted alphabetically

def listDirFilesRecursive(pathDir='./'):
    """Returns a list of all files and folders in a directory recursively."""
    listDir  = [path.join(dp, f) for dp, dn, filenames in walk(pathDir) for f in filenames]
    return sorted(listDir, key=str.lower)
    

def listToFile(li, name = "liste.md",  pathDir='./'):
    """Creates the file 'pathDir/name' from a given list and the pathDir."""
    try:
    	remove(pathDir + name)
    except(FileNotFoundError):
        pass
    with open(pathDir + name, "w", encoding="utf8") as f:
        f.write(f"# Liste des dossiers : \n`{Path().absolute()}`\n\n")
        for file in li:
            if not (name in file or "listDirectory.py" in file):
                f.write("- " + file + "\n")
        print(f"'{pathDir}liste.md' containing the list of files and folders was successfully created.")


def listToDictDir(listDir, pathDir='./'):
    """Returns a dictionary where the keys are directories and values are lists of files and directories in the folder."""
    dictDirR = dict()
    for elem in listDir:
        elemPath = pathDir + str(elem)
        if isfile(elemPath):
            # print(f"isfile {elemPath}")
            dictDirR[elem] = None
        elif isdir(elemPath):
            elemPath += '/'
            # print(f"isdir {elemPath}")
            dictDirR[elem] = listToDictDir(listDirFiles(elemPath), elemPath)
        else:
            # print(f"isNone {elemPath}")
            print(f"{elemPath} isn't a file or a folder.") # Should raise an exception
    return dictDirR


dictDir = listToDictDir(listDirFiles())
print(f"\nDictionaire :\n, {dictDir}\n")

listToFile(listDirFiles())

# diff /media/lilian/TOSHIBA\ EXT/Musique/liste.md liste.md -y --suppress-common-lines -w | less
