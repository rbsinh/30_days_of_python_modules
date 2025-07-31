import shutil
import os

shutil.copy("main.py","main2.py")

shutil.copytree("../28.Shutil","mytutorial")

shutil.move("../28.Shutil/main.py","main3.py")

shutil.rmtree("mytutorial")

os.remove("main2.py")

shutil.move("main3.py","main.py")
