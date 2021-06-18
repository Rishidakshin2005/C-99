import os
import shutil
src=input("entersourcefolder")
dest=input("enterDestinationFolder")

src=src+'/'
dest=dest+'/'

allfile=os.listdir(src)
for file in allfile:
    shutil.copy((src+file),dest)