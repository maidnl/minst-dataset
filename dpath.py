#!/usr/bin/python
# -*- coding: <<encoding>> -*-

# ------------------------------------------------------------------------------
# File with functions to deal with paths and files
# 1. Get list of directories inside a directory
# 2. Get list of files inside a directory
# 3. Extract zip file 
# ------------------------------------------------------------------------------
import os
from os import path
from os import rename
from os import listdir
import zipfile
import random
import string
from pprint import pprint

class PathNotExists(Exception):
   pass

class UnableToMakeDir(Exception):
   pass   

# ------------------------------------------------------------------------------
# Extract zip <file> in <folder>
# ------------------------------------------------------------------------------
def extract_zip(file, folder):
    if os.path.exists(file):
        zip_ref = zipfile.ZipFile(e, 'r')
        if not os.path.exists(folder):
            try:
                os.mkdir(folder)
            except:
                raise UnableToMakeDir
        zip_ref.extractall(folder)
        zip_ref.close()

# ------------------------------------------------------------------------------
# Get the lists of the directories
# Returns < [Absolute Directory Paths], [Directory Names (without path)] >
# Raises PathNotExists if folder does not exist
# ------------------------------------------------------------------------------

def get_folders_in_folder(folder):
    if os.path.exists(folder):
        # directories contenute in folder
        dirs = [f for f in os.listdir(folder) if path.isdir(os.path.join(folder,f))]
        # costruzione del path assoluto
        abs_dirs = [path.join(folder,f) for f in dirs]
        return abs_dirs, dirs
    else:
        raise PathNotExists  

# ------------------------------------------------------------------------------
# Get the lists of the file into the directory 
# <estens> filter to  a certain extension, could be a  list of extensions 
#    extension must be specified with "dot" .ext
# Return < [Absolute File Paths], [File names (without path)]
# Raises PathNotExists if folder does not exist
# ------------------------------------------------------------------------------
def get_files_in_folder(folder, extens = "all files"):
    if os.path.exists(folder):
        # files contenute in folder
        all_files = [f for f in os.listdir(folder) if path.isfile(os.path.join(folder,f))]
        if extens == "all files":
            files = all_files
        else:
            if not isinstance(extens,list): 
                ext = [extens]
            else:
                ext = extens    
            files = [f for f in all_files if path.splitext(f)[1] in ext]
        # costruzione del path assoluto
        abs_files = [path.join(folder,f) for f in files]
        return abs_files, files
    else:
        raise PathNotExists  

# Cancella tutti i files che hanno nel nome match
def delete_files_with_matches_name(folder, match, extens = 'all files'):
    abpaths , _ = get_files_in_folder(folder, extens)
    todelete = [f for f in abpaths if match in f]
    print("deleting ", len(todelete), " files")
    for f in todelete:
        try:
            os.remove(f)
        except:
            print("Unable to delete ", f)
        
    


   
if __name__ == "__main__":
    a,b = get_folders_in_folder('.') 
    print("Absolute path")
    print(a)
    print("Directory names")
    print(b)
    print("------------------------------------------------")
    a,b = get_files_in_folder('.') 
    print("Get file Absolute path")
    print(a)
    print("File names")
    print(b)
    print("------------------------------------------------")
    a,b = get_files_in_folder('.',".py") 
    print("Get file Absolute path")
    print(a)
    print("File names")
    print(b)
    print("------------------------------------------------")
    a,b = get_files_in_folder('.', [".py",".ini"]) 
    print("Get file Absolute path")
    print(a)
    print("File names")
    print(b)
    try:
        a,b = get_folders_in_folder('.\\topolino') 
    except:
        print("Directory does not exist")
    

    a,b = get_folders_in_folder('.\\images')
    print(a) 

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    delete_files_with_matches_name(path.join('.','images'), 'retro', extens = '.jpg')
    