import os
#os.system("date")
#os.mkdir ("C:/Users/Dell/Desktop/Module3/C-99/sourcefolder")


path="C:/Users/Dell/Desktop/Module3/C-99/sourcefolder"
isexist=os.path.exists(path)
print(isexist)
testpath="C:/Users/Dell/Desktop/Module3/C-99/OSModule.py"
splitpath=os.path.splitext(testpath)
print(splitpath[0]) 
print(splitpath[1])
