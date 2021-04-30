#Program to input file extensions
fileName=input("Write the file name")
file_extns=filename.split(".")
print("The extension is" +repr(file_extns[-1]))

#OUTPUT:
#Write the file name:abc.py
#The extension is 'py'
