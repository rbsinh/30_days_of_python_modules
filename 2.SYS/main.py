#sys --> sys module provides access to some variables used or maintained by interpreter

#os module --> interacting with the operating system,providing access to the underlying interface of the operating system

import sys
print(dir(sys)) #all functions
print(sys.path) # sys module is resposible for interacting with program and interpreter

for i in sys.path:
    print(i)


print(sys.version)

print(sys.version_info)

print(sys.getallocatedblocks())

def display(x):
    print("Python")
    print(x)

sys.displayhook==display

print(25)
