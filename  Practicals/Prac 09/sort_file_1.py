import os
import shutil

def main():
    source = "FileToSort"
    file_sort = os.listdir(source)

    for file in file_sort:
        if os.path.isdir(file):
            pass
        extension = file.spilt(".")[-1]
        if os.path.exists(source + '/' + extension):
            shutil.move(source + '/' + file, source + '/' + extension + '/' + file)
        else:
            os.mkdir(source + "/" + extension)
            shutil.move(source + '/' + file, source + '/' + extension + '/'+file)

main()
