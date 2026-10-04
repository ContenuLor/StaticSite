# Write a recursive function that copies all the contents from a source directory to a destination directory (in our case, static to public)
# It should first delete all the contents of the destination directory (public) to ensure that the copy is clean.
# It should copy all files and subdirectories, nested files, etc.
# I recommend logging the path of each file you copy, so you can see what's happening as you run and debug your code.

# Hook the function up to your main function and test it out. I didn't use a unit test for this one because it interacts with the file system: I just tested it manually.
# Add the public/ directory to your .gitignore file. This is where the generated site will live. As a general rule, it's bad to commit generated stuff, especially if it can be regenerated easily.
# Ensure that running main.sh generates the public directory and all the copied content correctly.
import os
import shutil

def copy_and_clean_public():
    source = "static"
    destination = "public"
    #check if "public" exists and delete it
    if os.path.exists(path=destination):
        shutil.rmtree(path=destination)
        
    #create public
    os.mkdir(path=destination)

    #initialize the copy
    copy_static(source,destination)

def copy_static(source,destination):

    #now need to copy files from "Static" to "Public"
    for item in os.listdir(path=source):
        item_path = os.path.join(source,item)
        if os.path.isfile(item_path):
            shutil.copy(item_path,destination)
        else:
            #create subfolder
            subfolder = os.path.join(destination,item)
            os.mkdir(path=subfolder)
            copy_static(item_path,subfolder)



