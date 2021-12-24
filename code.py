import os
import shutil

print("Welcome to the transfer of files and folders")
print("Please enter the full paths of files and folders below")
print("Thank you!")
path = int(input("Enter the file/folder you want to transfer : "))
folder = int(input("Enter the desination : "))

source = path
destination = folder

def transfer():
    des = shutil.move(source, destination)
    print("Move was successful!")
    print("New home of file/folder is: ", des)
    print("Have a good day!")

def exists():
    isExist = os.path.exists(path)
    des_isExist = os.path.exists(folder)

    if isExist == True:
        transfer()
    else :
        print("File or folder is not found")
    if des_isExist == True:
        transfer()
    else:
        print("Folder not found")

exists()
