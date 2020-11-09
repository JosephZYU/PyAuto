"""
⛳🦾 General Overview of Direcotry Management - June 27 2020

list all files of a directory
🌐 https://stackoverflow.com/a/3215392/12012157

Renaming multiple files in a directory
🌐 https://stackoverflow.com/a/37467669/12012157

get a directory listing sorted by creation date or modification date
🌐 https://stackoverflow.com/a/539024/12012157


"""

import os
import shutil
import glob
import datetime


# parameters
path_src = 'C:\\Users\\JosephYu\\Downloads\\'  # 👈
# path_dst = 'C:\\Users\\JosephYu\\Downloads'  # 👈
txt_ext = '.txt'  # 👈
mp4_ext = '.mp4'  # 👈


# * specify and update with current working dir 👑 os.chdir()
os.chdir(path_src)

# print(os.listdir())

# print current working directory to double confirm 👑 os.getcwd()
# print(os.getcwd())

"""# * list all items (everything) within the directory
# including files and folders 👑 os.listdir() - list everything in the dir

file_list_comprehension = [f for f in os.listdir(path_dst) if f.endswith(extension)]

for item in os.listdir():
    print(item)"""


"""# * create a list with all files *simple-version
# 👑 glob.glob('*.*') - anything with a dot . in between

all_list = glob.glob("*.*")

print(all_list)"""

"""# * ✅🦾 create list for files-only (excluding folders), get all-items(including folders) *advanced-version


def get_only_files(path):

    files_list = []

    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            files_list.append(file)

    return files_list


# print(get_only_files(path_src))

def count_files(path):

    os.chdir(path)

    print(len([name for name in os.listdir('.') if os.path.isfile(name)]))


count_files(path_src)


def get_all_items(path):

    items_list = []

    for item in os.listdir(path):
        items_list.append(item)

    return items_list


# print(get_all_items(path_src))"""

# * create a list with file in certain extension
# Optional - apply strip() to remove leading or trailing spaces
# 🌐 https://stackoverflow.com/a/10443548/12012157

txt_list = glob.glob("*.txt")  # pre-fix reference
mp4_list = glob.glob("*.mp4")  # the base reference

txt_root_list = glob.glob(f'{path_src}*.txt')
mp4_root_list = glob.glob(f'{path_src}*.mp4')

# sort files by creation date 👑 list.sort(key=os.path.getctime)
txt_list.sort(key=os.path.getctime)
mp4_list.sort(key=os.path.getctime)

txt_root_list.sort(key=os.path.getctime)
mp4_root_list.sort(key=os.path.getctime)

# print(txt_list)
# print(mp4_list)

# print(txt_root_list)
# print(mp4_root_list)

"""# * break file names into names and extensions
# 👑 os.path.splitext([list])
# org_name = original name of the file
# org_ext = original extension of the file

for file in txt_list:
    org_name, org_ext = os.path.splitext(file)
    print(org_name)
    print(org_ext)
    print()"""

# ✅🐱‍💻 now we need to further streamline⚡ the process with def function
# define empty list container
# 👀 make sure to use append() to add to list

# pass the target list of file names into the function (e.g. list = txt_list, mp4_list)
# create empty new list container and return the list


def get_name(list):

    org_name_list = []

    for file in list:
        org_name = os.path.splitext(file)[0]
        org_name_list.append(org_name)
    return org_name_list


def get_ext(list):

    org_ext_list = []

    for file in list:
        org_ext = os.path.splitext(file)[1]
        org_ext_list.append(org_ext)
    return org_ext_list


# * create the list of ✨ New Names for reference
ref_list = get_name(txt_list)   # 👈
target_list = get_name(mp4_list)  # 👈

ext_list = get_ext(mp4_list)  # 👈


# * ✅🦾 create dynamic time=stamp
# 👀 DO NOT place colon into file name (E.g. %H:%M)
now = datetime.datetime.now()
timestamp = now.strftime(" - %b-%d-%Y")  # 👈

new_name_list = []

for ref_name, file_name, ext_name in zip(ref_list, target_list, ext_list):
    new_name = f'{ref_name}{file_name}{timestamp}{ext_name}'
    new_name_list.append(new_name)

# print(new_name_list)


# * rename files with reference list
# ❗ we need to grab the files and directly apply from there
# our goals is to rename file in the root_directory list with updated new name

target_root_list = mp4_root_list  # 👈🚩

for file, name in zip(target_root_list, new_name_list):
    os.rename(file, os.path.join(path_src, name))  # 🦾🚩
