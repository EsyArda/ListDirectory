# ListDirectory

> Creates a file listing all files and directories in the current directory.

## Functions:

-  listDirFiles(pathDir='./'): 
    Returns the list of files and folders in a directory.

-   listDirFilesRecursive(pathDir='./'): 
    Returns a list of all files and folders in a directory recursively.

-   listToMd(li, name='liste.md', pathDir='./'): 
    Creates the file 'pathDir/name' from a given list and the pathDir.

-   listToDictDir(listDir, pathDir='./'): 
    Returns a dictionary where the keys are files of folders and values are lists of files and directories in the folder.

-   dictRecToMd(dic, name='liste.md', pathDir='./'): 
    Creates the file 'pathDir/name' from a given dictionary and the pathDir.

-   writeMd(dic, nbTabs=0): 
    Returns the string in Markdown to write from a dictionary.