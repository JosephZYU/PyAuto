
#* SUCCEED!!! Using Python to create directories and move files
# http://digitalcollections.wp.txstate.edu/2018/04/04/using-python-to-create-directories-and-move-files/

import os
import shutil

# C:\\Computer\\VSCode\\WIP_File_Moving\\Source_Data
# dir = "1959_6x6/"
dir = "C:\\Computer\\VSCode\\WIP_File_Moving\\Source_Data\\"

for file in os.listdir(dir):
    # get all but the last 8 characters to remove
    # the index number and extension
    dir_name = file[-11:-8]
    print(dir_name)
    print(f'dir_name: {dir_name}') #* WOW! f' makes it a dynamic function!

    fixed_name = file[:9] #*SOLVED 
    print(fixed_name)
    print(f'fixed_name: {fixed_name}')

    dir_path = dir + dir_name + '. ' + fixed_name # TODO: add TODAY function into the folder
    print(f'dir_path: {dir_path}')

    # check if directory exists or not yet
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    if os.path.exists(dir_path):
        file_path = dir + file
        print(f'file_path: {file_path}')
        
        # move files into created directory
        shutil.move(file_path, dir_path)

#? how to further rename EXPORT(1,2,3) dynamically with names ?
# key work search "Python rename files with list names"

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#* SOLVED find a way to retrieve text between '-' 
# https://stackoverflow.com/questions/4894069/regular-expression-to-return-text-between-parenthesis

# s = 'abcde(date=\'2/xc2/xb2\',time=\'/case/test.png\')'

s = 'abcde(Morning Joseph!)'

print(s[s.find("(")+1])
print(s.find("(")+1)

print(s[s.find(")")])
print(s.find(")"))

print(s[s.find("(")+1:s.find(")")])