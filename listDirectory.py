from os import listdir, remove, path, walk
from os.path import isfile, isdir
from pathlib import Path


def listDirFiles(pathDir='./'):
    """Returns the list of a directory content."""
    listDir = listdir(pathDir)
    # print("list : ", listDir)
    return sorted(listDir, key=str.lower)  # Sorted alphabetically

def listDirFilesRecursive(pathDir='./'):
    """Returns a list of the content of a directory recursively."""
    listDir  = [path.join(dp, f) for dp, dn, filenames in walk(pathDir) for f in filenames]
    return sorted(listDir, key=str.lower)
    

def listToMd(li, name = "liste.md",  pathDir='./'):
    """Creates the file 'pathDir/name' from a given list and the pathDir."""
    try:
    	remove(pathDir + name)
    except(FileNotFoundError):
        pass
    with open(pathDir + name, "w", encoding="utf8") as f:
        f.write(f"# Liste des dossiers : \n`{Path().absolute()}`\n\n")
        for file in li:
            if not (name in file or "listDirectory.py" in file):
                f.write("-\t" + file + "\n")
        print(f"'{pathDir}{name}' containing the list of files and folders was successfully created.")


def listToDictDir(listDir, pathDir='./'):
    """Returns a dictionary where the keys arethe content of the directory and their values are None if the key is a file and if it is a directory, it's content."""
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
            raise NotADirectoryError(f"{elemPath} isn't a file or a folder.")
    return dictDirR


def dictRecToMd(dic, name='list.md', pathDir='./'):
    """Creates the file 'pathDir/name' from a given dictionary and the pathDir."""
    # print("dictRecToMd :\n\n")
    try:
    	remove(pathDir + name)
    except(FileNotFoundError):
        pass
    with open(pathDir + name, "w", encoding="utf8") as f:
        f.write(f"# Liste des dossiers : \n`{Path().absolute()}`\n\n")
        f.write(writeMd(dic))
        # print(writeMd(dic))
        print(f"'{pathDir}{name}' containing the recursive list of files and folders was successfully created.")


def writeMd(dic, nbTabs=0):
    """Returns a string in Markdown listing the content of a dictionary."""
    text = ""
    # print(f"writeMd:\ntype(dic): {type(dic)}\ndic: {dic}\n")
    # print(dic.keys())
    for dir in dic:
        text += nbTabs * '\t'+ '-\t' + dir + '\n'
        # print(f"FOR: dir: `{dir}`, text: `{text}`, type(dic[dir]): `{type(dic[dir])}`")
        if dic[dir] is not None: # It's a folder
            text += writeMd(dic[dir], nbTabs + 1)
        else: # It is a file
            pass
    # print(f"text: {text}")
    return text


dictDir = listToDictDir(listDirFiles())
# print(f"\nDictionary :\n, {dictDir}\n")
# print(f"\nKeys :\n, {dictDir.keys()}\n")
# print(f"\nValues :\n, {dictDir.values()}\n")
dictRecToMd(dictDir)

# listToMd(listDirFiles())

# Compare two lists :
# diff /path/to/file.md file2.md -y --suppress-common-lines -w | less
