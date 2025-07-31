import os

#Check if path is exist or not
if(not os.path.exists("data")):
    os.mkdir("data")

#Iteration will be 0,1,2,3,4
#os.mkdir will new directory
for i in range(0,5):
    os.mkdir(f"data/day_{i+1}")

#os.rename will rename directory name
for i in range(0,3):
    os.rename(f"data/day_{i+1}",f"data/Tutorial_{i+1}")

#This will list all the directory inside folder
folders=os.listdir("data")

print(folders)

for folder in folders:
    print(folder)

#This will give you current working directory
print(os.getcwd())

#os.remove()-Will remove file

#os.rmdir()-remove an empty directory

#shutil.rmtree()-delete directory and all its content