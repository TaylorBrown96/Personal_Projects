import shutil
import os

'''
    This program rips out a level from the subdirectories from
    a top level directory and moves them to a set location.
'''

def main():
    try:
        src_path = 'C:/Users/forth/Desktop/Test1/'
        dst_path = 'C:/Users/forth/Desktop/Test1_Demo'

        fileDirectories = os.listdir(src_path)

        for folder in fileDirectories:
            subFolder = os.listdir(src_path + folder)
            shutil.move(src_path + folder + "/" + subFolder[0], dst_path)
        
        print("Migration Successful!")
    except:
        print("Migration Failed!")

if __name__ == "__main__":
    main()